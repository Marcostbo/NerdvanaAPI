from abc import ABC
from rest_framework import serializers


class GamePricingQuerySerializer(serializers.Serializer, ABC):
    game_id = serializers.IntegerField(required=True)
    console_id = serializers.IntegerField(required=True)


class GamePricingOutputSerializer(serializers, ABC):
    store_name = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=12)
    url = serializers.CharField()
