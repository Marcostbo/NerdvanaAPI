from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from nerdvanapp.models import PriceAlert, Games, Console
from nerdvanapp.serializers import PriceAlertDataSerializer, PriceAlertSerializer
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

        console_id = price_alert_data.validated_data.get('console_id')
        console = Console.objects.get(id=console_id).initials

        price = price_alert_data.validated_data.get('price')

        PriceAlert.objects.create(
            user=user,
            game=game,
            console=console,
            price=price
        )
        return HttpResponse(status=201)


class PriceAlertListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = self.request.user
        price_alerts = PriceAlert.objects.filter(
            user_id=user.id
        )

        return Response(PriceAlertSerializer(price_alerts, many=True).data)
