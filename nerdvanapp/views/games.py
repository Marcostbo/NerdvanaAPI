from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from nerdvanapp.models import Games
from nerdvanapp.serializers import FullGameSerializer, GameSerializer, SimpleGameSerializer, GameQuerySerializer
from nerdvanapp.views.utils.custom_basic_views import SerializerFilterView

import os
import requests


class GamesViewSet(ReadOnlyModelViewSet, SerializerFilterView):
    serializer_class = GameSerializer
    default_serializer = GameSerializer
    serializers = (GameSerializer, SimpleGameSerializer, FullGameSerializer)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        query_params = GameQuerySerializer(data=self.request.query_params)
        query_params.is_valid(raise_exception=True)

        name = query_params.validated_data.get('name')
        name_contains = query_params.validated_data.get('name_contains')
        company_id = query_params.validated_data.get('company_id')
        console_id = query_params.validated_data.get('console_id')
        top_games = query_params.validated_data.get('top_games')

        if name:
            games = Games.objects.filter(name__contains=name)
        elif name_contains:
            games = Games.objects.filter(name__contains=name_contains).filter(rating__isnull=False)
        elif company_id:
            games = Games.objects.filter(game_company__id=company_id).filter(rating__isnull=False)
        elif console_id:
            games = Games.objects.filter(console__in=[console_id]).filter(rating__isnull=False)
        elif top_games:
            games = Games.objects.filter(top_game=True)
        else:
            raise ValidationError('Select at least one filter')

        return games.filter(rating_count__gte=10).order_by('-rating')

    def retrieve(self, request, *args, **kwargs):
        game = get_object_or_404(Games, pk=kwargs.get('pk'))

        serializer = self.get_serializer_class()
        if not game.game_cover_link:
            try:
                game.game_cover_link = self.get_game_cover_link(game_name=game.name)
                game.save(update_fields=['game_cover_link'])
            except:
                pass
        return Response(serializer(game).data)

    @staticmethod
    def get_game_cover_link(game_name):
        cx_id = os.environ.get('CX_ID')
        google_api_key = os.environ.get('GOOGLE_API_KEY')

        query = f'"{game_name}" site: https: // howlongtobeat.com'
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cx_id}&key={google_api_key}&safe=high"

        response = requests.get(url, timeout=5)
        return response.json()['items'][0]['pagemap']['cse_image'][0]['src']
