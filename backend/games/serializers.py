from rest_framework import serializers
from .models import Games

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['title','year', 'factory_sealed', 'console', 'version']
        depth = 1