from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from nerdvanapp.serializers import SendEmailDataSerializer
from notification.models import ValidateEmailCode
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
        code_object = ValidateEmailCode.objects.get(code=code)

        validate_code_input(
            code_object=code_object,
            user=user
        )

        return HttpResponse(status=201)
