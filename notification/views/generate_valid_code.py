from rest_framework.response import Response
from rest_framework.views import APIView
from notification.serializers import GenerateCodeSerializer
from notification.methods.code_generator import CodeGenerator
from notification.models import PasswordRecoveryCode, ValidateEmailCode
from nerdvanapp.models import User
from datetime import datetime


class GenerateValidCodeView(APIView):

    def post(self):
        request = self.request
        request_data = GenerateCodeSerializer(request.data)
        request_data.is_valid(raise_exception=True)

        generated_code = CodeGenerator().generate_random_code(
            number_of_digits=6
        )
        reason = request_data.validated_data.get('reason')
        user = User.objects.all()
        if reason == 'Password Recovery':
            new_code = PasswordRecoveryCode.objects.create(
                user=1,
                code=generated_code,
                creation_date=datetime.now(),
                reason=reason
            )
        elif reason == 'Email Validation':
            b = 1
        else:
            raise ValueError

        return None

    # this view must:
    # generate code
        # receive number of digits
        # receive reason: validate_email or change_password
