from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from nerdvanapp.models import Games
from nerdvanapp.serializers import FullGameSerializer, GameSerializer, SimpleGameSerializer, GameQuerySerializer
from nerdvanapp.views.utils.custom_basic_views import SerializerFilterView, PaginatedViewSet

import os, requests


class GameListView(APIView, SerializerFilterView, PaginatedViewSet):
    serializer_class = GameSerializer
    default_serializer = GameSerializer
    serializers = (GameSerializer, SimpleGameSerializer, FullGameSerializer)

    def get(self, request):
        query_params = GameQuerySerializer(data=self.request.query_params)
        query_params.is_valid(raise_exception=True)

        name = query_params.validated_data.get('name')
        name_contains = query_params.validated_data.get('name_contains')
        company_id = query_params.validated_data.get('company_id')
        console_id = query_params.validated_data.get('console_id')

        if name:
            games = Games.objects.filter(name__contains=name)
        elif name_contains:
            games = Games.objects.filter(name__contains=name_contains).filter(rating__isnull=False)
        elif company_id:
            games = Games.objects.filter(game_company__id=company_id).filter(rating__isnull=False)
        elif console_id:
            games = Games.objects.filter(console__in=[console_id]).filter(rating__isnull=False)
        else:
            raise ValidationError('Select at least one filter')

        games = games.filter(rating_count__gte=10).order_by('-rating')
        serializer = self.get_serializer_class()
        paginated_games, headers = self.paginate_queryset(
            queryset=games
        )

        return Response(serializer(paginated_games, many=True).data, headers=headers)


class GameView(APIView, SerializerFilterView):
    serializer_class = GameSerializer
    default_serializer = GameSerializer
    serializers = (GameSerializer, SimpleGameSerializer, FullGameSerializer)

    def get(self, request, pk=None):
        game_id = pk
        game = self.get_object_by_pk(game_id)

        serializer = self.get_serializer_class()
        if not game.game_cover_link:
            try:
                game.game_cover_link = self.get_game_cover_link(game_name=game.name)
                game.save(update_fields=['game_cover_link'])
            except:
                pass
        return Response(serializer(game).data)

    @staticmethod
    def get_object_by_pk(pk):
        try:
            return Games.objects.get(pk=pk)
        except Games.DoesNotExist:
            raise Http404

    @staticmethod
    def get_game_cover_link(game_name):
        cx_id = os.environ.get('CX_ID')
        google_api_key = os.environ.get('GOOGLE_API_KEY')

        query = f'"{game_name}" site: https: // howlongtobeat.com'
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cx_id}&key={google_api_key}&safe=high"

        response = requests.get(url, timeout=5)
        return response.json()['items'][0]['pagemap']['cse_image'][0]['src']
