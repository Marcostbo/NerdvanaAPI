from rest_framework import serializers
from nerdvanapp.models import Games
from .game_company import GameCompanySerializer


class GameQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    name_contains = serializers.CharField(required=False)
    company_id = serializers.IntegerField(required=False)
    console_id = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError

    def validate(self, data):
        game_filters = (data.get('name'), data.get('name_contains'), data.get('company_id'), data.get('console_id'))
        number_of_filters = sum([0 if info is None else 1 for info in game_filters])
        if number_of_filters > 1:
            raise serializers.ValidationError('Specify only one filter')
        if number_of_filters == 0:
            raise serializers.ValidationError('Specify at least one filter')
        return data


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = "__all__"
        api_filter_name = 'game_serializer'


class FullGameSerializer(serializers.ModelSerializer):
    game_company = GameCompanySerializer()

    class Meta:
        model = Games
        fields = "__all__"
        api_filter_name = 'full_game_serializer'


class SimpleGameSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError

    class Meta:
        model = Games
        fields = ('id', 'name', 'release',)
        api_filter_name = 'simple_game_serializer'
