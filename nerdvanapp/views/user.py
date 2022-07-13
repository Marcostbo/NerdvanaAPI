from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from nerdvanapp.serializers import UserSerializer
from rest_framework.response import Response
from nerdvanapp.models import User
import jwt


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