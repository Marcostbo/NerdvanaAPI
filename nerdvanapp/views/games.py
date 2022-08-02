from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from nerdvanapp.models import Games
from nerdvanapp.serializers import FullGameSerializer, GameSerializer, SimpleGameSerializer, GameQuerySerializer
from nerdvanapp.views.utils.custom_basic_views import SerializerFilterView


class GameListView(APIView, SerializerFilterView):
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

        serializer = self.get_serializer_class()

        return Response(serializer(games, many=True).data)


class GameView(APIView, SerializerFilterView):
    serializer_class = GameSerializer
    default_serializer = GameSerializer
    serializers = (GameSerializer, SimpleGameSerializer, FullGameSerializer)

    def get(self, request, pk=None):
        game_id = pk
        game = self.get_object(game_id)

        serializer = self.get_serializer_class()
        return Response(serializer(game).data)

    @staticmethod
    def get_object(pk):
        try:
            return Games.objects.get(pk=pk)
        except Games.DoesNotExist:
            raise Http404
