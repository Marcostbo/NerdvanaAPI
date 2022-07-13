from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from nerdvanapp.models import User


class LoginView(APIView):

    def get(self, request):
        email = request.data['email']
        password = request.data['password']

        user = self.validate_user_and_password(
            email=email,
            password=password
        )

        return Response({
            'email': user.email,
            'status': 'validated'
        })

    @staticmethod
    def validate_user_and_password(email, password):
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        return user
