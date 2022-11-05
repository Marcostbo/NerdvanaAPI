from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from nerdvanapp.serializers import UserSerializer
from rest_framework.response import Response


class SendEmailValidateCode(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return None
