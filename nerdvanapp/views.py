from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from nerdvanapp.serializers import UserSerializer
from rest_framework.response import Response
from .models import User
import jwt
import datetime


class RegisterView(APIView):
    @staticmethod
    def post(request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()

        return Response(user.data)


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


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        user = self.get_user_via_token(
            token=token
        )

        return Response(UserSerializer(user).data)

    @staticmethod
    def get_user_via_token(token):
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
            user_id = payload.get('id')
            user = User.objects.filter(id=user_id).first()
            return user
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return Response(response)
