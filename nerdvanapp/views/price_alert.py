from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from nerdvanapp.models import PriceAlert
from nerdvanapp.serializers import PriceAlertModelSerializer, PriceAlertModelFullSerializer

from nerdvanapp.views.utils.custom_basic_views import SerializerFilterView


class PriceAlertViewSet(SerializerFilterView, ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = PriceAlertModelSerializer
    default_serializer = PriceAlertModelSerializer
    serializers = (PriceAlertModelSerializer, PriceAlertModelFullSerializer, )

    def get_queryset(self):
        user = self.request.user
        return PriceAlert.objects.filter(user_id=user.id)

    def create(self, request, *args, **kwargs):
        # This create method act as proxy to the create method in mixins.CreateModelMixin
        if not request.user.id == int(request.data.get('user')):
            raise PermissionDenied
        return super().create(request, *args, **kwargs)
