from rest_framework.response import Response
from rest_framework.views import APIView
from notification.methods import code_generator


class GenerateValidCodeView(APIView):

    def post(self):
        request = self.request
        return None

    # this view must:
    # generate code
