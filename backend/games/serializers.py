from rest_framework import serializers
from .models import Game

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'cost', 'year', 'console', 'version', 'user', 'user_id', 'image']
        depth = 1