from rest_framework import serializers
from .models import Player, SavedPlayers

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('summoner_name', 'summoner_id', 'summoner_level', 'profile_icon_id', 'saved_players')

class SavedPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedPlayers
        fields = ('saved_players', 'user')

# Path: lolMastery\players\views.py


