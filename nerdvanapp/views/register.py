from rest_framework.views import APIView
from nerdvanapp.serializers import UserSerializer
from rest_framework.response import Response


class RegisterView(APIView):
    @staticmethod
    def post(request):
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()

        return Response(user.data)
