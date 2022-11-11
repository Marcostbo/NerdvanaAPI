from rest_framework import serializers


class PasswordRecoverySerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    code = serializers.IntegerField(required=True)
    user_email = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
