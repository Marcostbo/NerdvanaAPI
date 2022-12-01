from rest_framework.views import APIView
from nerdvanapp.serializers import SendEmailDataSerializer
from notification.models import PasswordRecoveryCode
from notification.methods import SendNotification
from nerdvanapp.models import User
from nerdvanapp.views.utils.functions import validate_code_input
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


class SendEmailPasswordRecoveryView(APIView):

    def post(self, request):
        data = SendEmailDataSerializer(data=self.request.data)
        data.is_valid(raise_exception=True)

        code = data.validated_data.get('code')
        user_id = data.validated_data.get('user')

        user = get_object_or_404(User, pk=user_id)
        code_object = PasswordRecoveryCode.objects.get(code=code)

        validate_code_input(
            code_object=code_object,
            user=user
        )

        text = f'Olá, {user.first_name} \n' \
               f'\n'\
               f'Nós recebemos uma solicitação para alteração da senha de sua conta no Nerdvana. \n' \
               f'\n' \
               f'Código de recuperação: {code} \n' \
               f'\n' \
               f'Este código é válido por 5 minutos e não deve ser compartilhado com terceiros. \n' \
               f'\n' \
               f'Se você não solicitou este código, pode ignorar com segurança este e-mail. \n' \
               f'Outra pessoa pode ter digitado seu endereço de e-mail por engano. \n' \
               f'\n' \
               f'Obrigado'

        SendNotification().send_email(
            to_email=user.email,
            subject='Login Nerdvana - Recuperação de Senha',
            message=text,
            user=user,
            reason="Password Recovery"
        )

        return HttpResponse(status=201)
