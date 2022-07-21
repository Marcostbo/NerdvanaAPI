from rest_framework import serializers
from nerdvanapp.models import Games


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ('id', 'name', 'release',
                  'summary', 'storyline',
                  'console', 'game_company',
                  'rating', 'rating_count',)
