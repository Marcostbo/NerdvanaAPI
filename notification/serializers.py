from rest_framework import serializers


class GenerateCodeSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    code = serializers.IntegerField(required=True)
    user = serializers.IntegerField(required=True)
    reason = serializers.CharField(required=True)
