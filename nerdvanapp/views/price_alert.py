from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from nerdvanapp.models import PriceAlert
from nerdvanapp.serializers import PriceAlertModelSerializer, PriceAlertModelFullSerializer
from rest_framework.response import Response

from nerdvanapp.views.utils.custom_basic_views import SerializerFilterView


class PriceAlertViewSet(ModelViewSet, SerializerFilterView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PriceAlertModelSerializer
    default_serializer = PriceAlertModelSerializer
    serializers = (PriceAlertModelSerializer, PriceAlertModelFullSerializer, )

    def get_queryset(self):
        user = self.request.user
        return PriceAlert.objects.filter(user_id=user.id)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
