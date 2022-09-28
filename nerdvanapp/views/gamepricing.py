from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from nerdvanapp.models import Games, Console, Store
from nerdvanapp.serializers import GamePricingQuerySerializer, GamePricingOutputSerializer


class GamePricingView(APIView):
    serializer_class = GamePricingOutputSerializer
    default_serializer = GamePricingOutputSerializer

    def get(self, request):
        query_params = GamePricingQuerySerializer(data=self.request.data)
        query_params.is_valid(raise_exception=True)

        game_name = self.get_game_name(
            game_id=query_params.validated_data.get('game_id')
        )
        console_initials = self.get_console_initials(
            console_id=query_params.validated_data.get('console_id')
        )
        stores_object = self.get_all_stores_object()

    @staticmethod
    def get_game_name(game_id):
        try:
            return Games.objects.get(pk=game_id).name
        except Games.DoesNotExist:
            raise Http404

    @staticmethod
    def get_console_initials(console_id):
        try:
            return Console.objects.get(pk=console_id).initials
        except Console.DoesNotExist:
            raise Http404

    @staticmethod
    def get_all_stores_object():
        return Store.objects.all().values_list('search_name', 'link')
