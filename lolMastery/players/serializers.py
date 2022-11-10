from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['summoner_name', 'summoner_id', 'saved_players', 'summoner_level', 'profile_icon_id']

