from rest_framework.response import Response
from rest_framework.views import APIView
from notification.serializers import GenerateCodeRequestSerializer, NewCodeSerializer
from notification.methods.code_generator import CodeGenerator
from notification.models import PasswordRecoveryCode, ValidateEmailCode
from nerdvanapp.models import User
from datetime import datetime
from django.shortcuts import get_object_or_404


class GenerateValidCodeView(APIView):

    def post(self):
        request = self.request
        request_data = GenerateCodeRequestSerializer(request.data)
        request_data.is_valid(raise_exception=True)

        generated_code = CodeGenerator().generate_random_code(
            number_of_digits=6
        )
        reason = request_data.validated_data.get('reason')
        user_id = request_data.validated_data.get('user')
        user = get_object_or_404(User, pk=user_id)
        if reason == 'Password Recovery':
            new_code = PasswordRecoveryCode.objects.create(
                user=user,
                code=generated_code,
                creation_date=datetime.now(),
                reason=reason
            )
        elif reason == 'Email Validation':
            new_code = ValidateEmailCode.objects.create(
                user=user,
                code=generated_code,
                creation_date=datetime.now(),
                reason=reason
            )
        else:
            raise ValueError

        return Response(NewCodeSerializer(new_code).data)
