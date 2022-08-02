from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from nerdvanapp.models import Games
from nerdvanapp.serializers import GameSerializer, SimpleGameSerializer, GameQuerySerializer


class GameListView(APIView):
    serializer_class = GameSerializer
    serializers = (GameSerializer, SimpleGameSerializer,)

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
            games = Games.objects.filter(name__contains=name).filter(rating__isnull=False)
        elif company_id:
            games = Games.objects.filter(game_company__id=company_id).filter(rating__isnull=False)
        elif console_id:
            games = Games.objects.filter(console__in=[console_id]).filter(rating__isnull=False)
        else:
            raise ValidationError('Select at least one filter')

        return Response(GameSerializer(games, many=True).data)


class GameView(APIView):
    serializer_class = GameSerializer
    serializers = (GameSerializer, SimpleGameSerializer,)

    def get(self, request, pk=None):
        game_id = pk
        game = self.get_object(game_id)
        return Response(GameSerializer(game).data)

    @staticmethod
    def get_object(pk):
        try:
            return Games.objects.get(pk=pk)
        except Games.DoesNotExist:
            raise Http404
