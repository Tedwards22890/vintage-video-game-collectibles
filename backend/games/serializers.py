from rest_framework import serializers
from .models import Game

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title','year', 'factory_sealed', 'console', 'version']
        depth = 1