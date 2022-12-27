from rest_framework import serializers
from .models import Game

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'description', 'cost', 'year', 'factory_sealed', 'console', 'version', 'user', 'user_id', 'image1', 'image2', 'image3', 'image4', 'image5']
        depth = 1