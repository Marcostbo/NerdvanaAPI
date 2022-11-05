from rest_framework import serializers


class SendEmailDataSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    code = serializers.IntegerField(required=True)
