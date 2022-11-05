from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from nerdvanapp.serializers import SendEmailDataSerializer
from notification.models import ValidateEmailCode
from notification.methods import SendNotification
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class SendEmailValidateCode(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = SendEmailDataSerializer(data=self.request.data)
        data.is_valid(raise_exception=True)

        code = data.validated_data.get('Code')
        user = self.request.user

        code_object = ValidateEmailCode.objects.get(code=code)
        if not code_object:
            raise ValidationError('Code does not exists')
        elif code_object.user != user:
            raise ValidationError('Invalid code for this user')



        return None
