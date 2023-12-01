from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from nerdvanapp.models import User
from nerdvanapp.serializers import UserSerializer


class RegisterViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    @action(detail=True, methods=['patch'], url_path='update-register', permission_classes=(IsAuthenticated,))
    def patch(self, request, pk=None):
        user = self.get_object()
        if user.id != self.request.user.id:
            raise PermissionDenied
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='inactivate-profile', permission_classes=(IsAuthenticated,))
    def inactivate_profile(self, request, pk=None):
        user = self.get_object()
        if user.id != self.request.user.id:
            raise PermissionDenied

        user.is_active = False
        user.save(update_fields=['is_active'])

        return Response(status=status.HTTP_201_CREATED)
