from rest_framework import serializers


class PriceAlertDataSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    game_id = serializers.IntegerField(required=True)
    price = serializers.DecimalField(required=True, decimal_places=2, max_digits=8)
