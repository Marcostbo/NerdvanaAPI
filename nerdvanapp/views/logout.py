from rest_framework.views import APIView
from rest_framework.response import Response


class LogoutView(APIView):
    @staticmethod
    def post():
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return Response(response)
