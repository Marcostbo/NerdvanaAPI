from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from nerdvanapp.methods.game_pricing import GamePricing
from nerdvanapp.models import Games, Console, Store
from nerdvanapp.serializers import GamePricingQuerySerializer, GamePricingOutputSerializer, StoresSerializer


class GamePricingView(APIView):
    serializer_class = GamePricingOutputSerializer
    default_serializer = GamePricingOutputSerializer

    def get(self, request):
        query_params = GamePricingQuerySerializer(data=self.request.query_params)
        query_params.is_valid(raise_exception=True)

        game_name = self.get_game_name(
            game_id=query_params.validated_data.get('game_id')
        )
        console_initials = self.get_console_initials(
            console_id=query_params.validated_data.get('console_id')
        )
        stores_object = self.get_all_stores_object()

        game_price = GamePricing()
        price_result = game_price.get_smaller_price_and_url_for_multiple_stores_v2(
            game=game_name,
            console=console_initials,
            stores_list=stores_object
        )
        price_result = sorted(price_result, key=lambda d: float(d['price']))
        return Response(GamePricingOutputSerializer(price_result, many=True).data)

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
        return Store.objects.all().values_list('search_name', 'link', 'name')
