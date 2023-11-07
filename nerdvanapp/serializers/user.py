from rest_framework import serializers
from nerdvanapp.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'first_name', 'last_name', 'email', 'is_active', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if not instance.name:
            instance.name = f'{instance.first_name} + {instance.last_name}'
        if password is not None:
            instance.set_password(password)  # Save hashed password
            instance.is_active = True
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
            instance.save(update_fields=['password'])
        return super().update(instance, validated_data)
