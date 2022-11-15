from django.db import models

# Create your models here.

from django.db import models
from django.contrib.postgres.fields import ArrayField, CITextField
from django.forms import CharField
from django.contrib.auth.models import User

class SavedPlayers(models.Model):

    saved_players = ArrayField(models.CharField(max_length=200), default=list)
    # tem um usuario associado a ele
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.summoner_name

class Player(models.Model):
    # The player name, as it appears in-game, do not differentiate between upper and lower case
    summoner_name = models.CharField(max_length=16, primary_key=True)
    #summoner id can be null and is a mix of numbers and letters
    summoner_id = models.CharField(max_length=200, null=True)
    # A list of saved players to be displayed in the index page of the app, starts empty and is a list of objects, and can not have repeated values or duplicated values
    saved_players = models.ForeignKey(SavedPlayers, on_delete=models.CASCADE, null=True)
    # User level
    summoner_level = models.IntegerField(null=True)
    # User icon
    profile_icon_id = models.IntegerField(null=True)


    def __str__(self):
        return self.summoner_name + " " + str(self.summoner_id) + " " + str(self.saved_players)



        