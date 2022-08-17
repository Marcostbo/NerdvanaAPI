from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from nerdvanapp.models import Games
from nerdvanapp.serializers import GameSerializer, FullGameSerializer, RecommenderQuerySerializer


class GameRecommenderView(APIView):
    default_serializer = GameSerializer
    serializers = (GameSerializer, FullGameSerializer)

    def get(self, request):
        request = self.request
        recommender_params = RecommenderQuerySerializer(data=request.data)
        recommender_params.is_valid(raise_exception=True)

        game_id = recommender_params.validated_data.get('game_id')
        console_id = recommender_params.validated_data.get('console_id')
        number_of_recommendations = recommender_params.validated_data.get('number_of_recommendations')

        selected_game = self.get_game_for_recommendation(pk=game_id)
        list_of_games = self.get_list_of_games_for_recommendation(console_id=console_id)

        return None

    @staticmethod
    def get_game_for_recommendation(pk):
        try:
            return Games.objects.get(pk=pk)
        except Games.DoesNotExist:
            raise Http404

    @staticmethod
    def get_list_of_games_for_recommendation(console_id):
        games = Games.objects.filter(console__in=[console_id]).filter(rating__isnull=False)
        return games
