from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from nerdvanapp.models import User
import jwt
import datetime


class LoginView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = self.validate_user_and_password(
            email=email,
            password=password
        )

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm="HS256")

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'user': user.email,
            'token': token
        }
        return response

    @staticmethod
    def validate_user_and_password(email, password):
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        return user