from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from nerdvanapp.serializers import SendEmailDataSerializer
from notification.models import ValidateEmailCode
from notification.methods import SendNotification
from nerdvanapp.views.utils.functions import validate_code_input
from django.http import HttpResponse


class SendEmailValidateCodeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = SendEmailDataSerializer(data=self.request.data)
        data.is_valid(raise_exception=True)

        code = data.validated_data.get('code')
        user = self.request.user

        code_object = ValidateEmailCode.objects.get(code=code)

        validate_code_input(
            code_object=code_object,
            user=user
        )

        text = f'Olá, {user.first_name} \n' \
               f'\n'\
               f'Nós recebemos uma solicitação para um código de validação para a sua conta no Nerdvana. \n' \
               f'\n' \
               f'Código de ativação: {code} \n' \
               f'\n' \
               f'Este código é válido por 5 minutos e não deve ser compartilhado com terceiros. \n' \
               f'\n' \
               f'Se você não solicitou este código, pode ignorar com segurança este e-mail. \n' \
               f'Outra pessoa pode ter digitado seu endereço de e-mail por engano. \n' \
               f'\n' \
               f'Obrigado'

        SendNotification.send_email_proxy(
            to_email=user.email,
            subject='Login Nerdvana - Código de Validação',
            message=text,
            user_id=user.id,
            reason="Email Validation"
        )

        return HttpResponse(status=201)


class ValidateEmailView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = SendEmailDataSerializer(data=self.request.data)
        data.is_valid(raise_exception=True)

        code = data.validated_data.get('code')
        user = self.request.user

        code_object = ValidateEmailCode.objects.get(code=code)

        validate_code_input(
            code_object=code_object,
            user=user
        )

        user.validate()

        return HttpResponse(status=201)
