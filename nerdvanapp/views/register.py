from rest_framework.views import APIView
from nerdvanapp.serializers import UserSerializer
from rest_framework.response import Response


class RegisterView(APIView):
    @staticmethod
    def post(request):
        # Build user input data
        user_data = request.data.copy()
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        user_data['name'] = f'{first_name} {last_name}'
        # Serialize and create user
        user = UserSerializer(data=user_data)
        user.is_valid(raise_exception=True)
        user.save()

        return Response(user.data)
