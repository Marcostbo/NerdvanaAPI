from rest_framework import serializers
from nerdvanapp.models import Games
from nerdvanapp.serializers import GameCompanySerializer


class GameQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    company_id = serializers.IntegerField(required=False)
    console_id = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = "__all__"


class FullGameSerializer(serializers.ModelSerializer):
    game_company = GameCompanySerializer()

    class Meta:
        model = Games
        fields = "__all__"


class SimpleGameSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError

    class Meta:
        model = Games
        fields = ('id', 'name', 'release',)
