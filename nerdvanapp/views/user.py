from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from nerdvanapp.models import User
from notification.models import PasswordRecoveryCode
from nerdvanapp.serializers import UserSerializer, PasswordRecoverySerializer
from nerdvanapp.views.utils.functions import validate_code_input
from rest_framework.response import Response
from django.http import HttpResponse


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        return Response(UserSerializer(user).data)


class ChangePasswordView(APIView):

    def put(self, request):
        """ Method to update user's password """

        data = PasswordRecoverySerializer(data=self.request.data)
        data.is_valid(raise_exception=True)

        user_email = data.validated_data.get('user_email')
        user = User.objects.get(email=user_email)

        code = data.validated_data.get('code')
        code_object = PasswordRecoveryCode.objects.get(code=code)

        validate_code_input(
            code_object=code_object,
            user=user
        )

        new_password = data.validated_data.pop('new_password')
        user.change_password(
            new_password=new_password
        )

        return HttpResponse(status=202)
