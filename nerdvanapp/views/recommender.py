from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from nerdvanapp.models import Games
from nerdvanapp.serializers import GameSerializer


class GameRecommenderView(APIView):
    default_serializer = GameSerializer

    def get(self):
        request = self.request
        return None
