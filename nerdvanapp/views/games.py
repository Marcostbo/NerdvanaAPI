from rest_framework.views import APIView
from rest_framework.response import Response
from nerdvanapp.models import Games
from nerdvanapp.serializers import GameSerializer, GameQuerySerializer


class GameView(APIView):
    serializer_class = GameSerializer

    def get(self, request):
        query_params = GameQuerySerializer(data=self.request.query_params)
        query_params.is_valid(raise_exception=True)

        name = query_params.validated_data.get('name')
        game = Games.objects.filter(name=name)

        return Response(GameSerializer(game, many=True).data)
