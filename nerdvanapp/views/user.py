from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from nerdvanapp.serializers import UserSerializer
from rest_framework.response import Response


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = self.request.user

        return Response(UserSerializer(user).data)
