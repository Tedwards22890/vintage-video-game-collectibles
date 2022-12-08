from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user','user_id', 'game', 'game_id', 'payment_processed']
        depth = 1