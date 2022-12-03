from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from nerdvanapp.models import PriceAlert, Games
from nerdvanapp.serializers import PriceAlertDataSerializer
from rest_framework.response import Response
from django.http import HttpResponse


class PriceAlertCreateView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = self.request.user

        price_alert_data = PriceAlertDataSerializer(data=self.request.data)
        price_alert_data.is_valid(raise_exception=True)

        game_id = price_alert_data.validated_data.get('game_id')
        game = Games.objects.get(id=game_id)

        price = price_alert_data.validated_data.get('price')

        PriceAlert.objects.create(
            user=user,
            game=game,
            price=price
        )
        return HttpResponse(status=201)
