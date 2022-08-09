from rest_framework import serializers


class RecommenderQuerySerializer(serializers.Serializer):
    game_id = serializers.IntegerField(required=True)
    console_id = serializers.IntegerField(required=True)
    number_of_recommendations = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        raise NotImplementedError
