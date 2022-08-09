from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from nerdvanapp.models import Games
from nerdvanapp.serializers import GameSerializer, FullGameSerializer, RecommenderQuerySerializer


class GameRecommenderView(APIView):
    default_serializer = GameSerializer
    serializers = (GameSerializer, FullGameSerializer)

    def get(self):
        request = self.request
        query_params = RecommenderQuerySerializer(data=request.data)
        query_params.is_valid(raise_exception=True)
        return None
