from rest_framework import serializers
from nerdvanapp.serializers import UserSerializer


class GenerateCodeRequestSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    user = serializers.IntegerField(required=False)
    reason = serializers.CharField(required=True)


class NewCodeSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    user = UserSerializer()
    code = serializers.CharField(required=True)
    creation_date = serializers.CharField()
    valid_until = serializers.DateTimeField()
