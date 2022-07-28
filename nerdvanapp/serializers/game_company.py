from rest_framework import serializers
from nerdvanapp.models import GameCompany


class GameCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCompany
        fields = "__all__"
