from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from nerdvanapp.methods.game_recommender import GameRecommender
from nerdvanapp.models import Games
from nerdvanapp.serializers import GameSerializer, FullGameSerializer, RecommenderQuerySerializer


class GameRecommenderView(APIView):
    default_serializer = GameSerializer
    serializers = (GameSerializer, FullGameSerializer)

    def get(self, request):
        request = self.request
        recommender_params = RecommenderQuerySerializer(data=request.query_params)
        recommender_params.is_valid(raise_exception=True)

        game_id = recommender_params.validated_data.get('game_id')
        console_id = recommender_params.validated_data.get('console_id')
        number_of_recommendations = recommender_params.validated_data.get('number_of_recommendations')

        selected_game = self.get_game_for_recommendation(pk=game_id)
        list_of_games = self.get_list_of_games_for_recommendation(console_id=console_id)

        list_of_games = self.verify_if_game_is_in_list_of_games(
            selected_game=selected_game,
            list_of_games=list_of_games
        )

        recommended_games = self.get_full_recommendation(
            list_of_games=list_of_games,
            game_id=game_id,
            number_of_recommendations=number_of_recommendations
        )

        return Response(GameSerializer(recommended_games, many=True).data)

    @staticmethod
    def get_game_for_recommendation(pk):
        try:
            return Games.objects.filter(pk=pk).values_list('id', 'summary').first()
        except Games.DoesNotExist:
            raise Http404

    @staticmethod
    def get_list_of_games_for_recommendation(console_id):
        games = Games.objects.filter(console__in=[console_id]).filter(rating__isnull=False).values_list('id', 'summary')
        return games

    @staticmethod
    def verify_if_game_is_in_list_of_games(selected_game, list_of_games):

        game_id = selected_game[0]

        is_in_list = list_of_games.filter(id=game_id).exists()
        if not is_in_list:
            list_of_games = list(list_of_games)
            list_of_games.append(selected_game)
        else:
            list_of_games = list(list_of_games)

        return list_of_games

    @staticmethod
    def get_full_recommendation(list_of_games, game_id, number_of_recommendations):
        game_recommender = GameRecommender(
            game_data=list_of_games
        )

        game_recommender.create_tfidf_matrix()
        game_recommender.create_cosine_similarities(game_id=game_id)
        recommendations = game_recommender.recommend(
            game_id=game_id,
            number_of_recommendations=number_of_recommendations
        )
        recommendations_ids = [rec[1] for rec in recommendations]
        recommended_games = Games.objects.filter(id__in=recommendations_ids)

        return recommended_games
