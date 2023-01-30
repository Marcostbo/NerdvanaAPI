from rest_framework import serializers
from nerdvanapp.models import Games, Console, Store


class GamePricingQuerySerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    game_id = serializers.IntegerField(required=True)
    console_id = serializers.IntegerField(required=True)


class GamePricingOutputSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    store_name = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=12, allow_null=True, required=False)
    url = serializers.CharField(allow_null=True, required=False)


class StoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('search_name', 'link',)
