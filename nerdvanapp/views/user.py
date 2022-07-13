from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from nerdvanapp.serializers import UserSerializer
from rest_framework.response import Response
from nerdvanapp.models import User
import jwt


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        user = request.user

        return Response(UserSerializer(user).data)
