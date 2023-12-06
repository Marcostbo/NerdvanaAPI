from rest_framework import serializers

from nerdvanapp.models import PriceAlert
from nerdvanapp.serializers import SimpleGameSerializer


class PriceAlertModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceAlert
        fields = "__all__"
        api_filter_name = 'default'

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(
            **validated_data
        )
        return instance


class PriceAlertModelFullSerializer(PriceAlertModelSerializer):
    game = SimpleGameSerializer()

    class Meta:
        model = PriceAlert
        fields = "__all__"
        api_filter_name = 'full_price_alert'
