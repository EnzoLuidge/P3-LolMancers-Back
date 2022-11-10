from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Player
from .serializers import PlayerSerializer
from rest_framework import status



@api_view(['GET', 'POST', 'DELETE'])
# The api retrives or creates the user when get is called, update the user name when post is called, also deletes the user when delete is called.
def User(request):
    if request.method == 'GET':
        try:
            user = Player.objects.get(summoner_name=request.GET['summoner_name'])
        except Player.DoesNotExist:
            #create a new user in the database
            user = Player(summoner_name=request.GET['summoner_name'])
            user.save()
        serializer = PlayerSerializer(user)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            user = Player.objects.get(summoner_name=request.GET['summoner_name'])
        except Player.DoesNotExist:
            raise Http404
        serializer = PlayerSerializer(user, data=request.data) # request.data is the data sent from the front end in json format.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            user = Player.objects.get(summoner_name=request.GET['summoner_name'])
        except Player.DoesNotExist:
            raise Http404
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
# The api retreves all users when get is called, creates a new user when post is called, and deletes all users when delete is called.
def User_operations(request):
    try:
        if request.method == 'GET':
            users = Player.objects.all()
            serializer = PlayerSerializer(users, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            # Se o usuario ja existe, não adiciona
            try:
                user = Player.objects.get(summoner_name=request.data['summoner_name'])
                return Response(status=status.HTTP_208_ALREADY_REPORTED)
            except Player.DoesNotExist:
                serializer = PlayerSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            users = Player.objects.all()
            users.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        raise Http404

@api_view(['GET', 'POST', 'DELETE'])
# the api get the saved players when it is called, create a a new saved player and add it to the list when post is called, and deletes a saved players when delete is called.
def Saved_player_operations(request):
    if request.method == 'GET':
        try:
            user = Player.objects.get(summoner_name=request.GET['summoner_name'])
        except Player.DoesNotExist:
            raise Http404
        return Response(user.saved_players)
    elif request.method == 'POST':
        try:
            user = Player.objects.get(summoner_name=request.GET['summoner_name'])
        except Player.DoesNotExist:
            raise Http404
        user.saved_players.append(request.GET['saved_player'])
        user.save()
        return Response(user.saved_players, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        try:
            user = Player.objects.get(summoner_name=request.GET['summoner_name'])
        except Player.DoesNotExist:
            raise Http404
        user.saved_players.remove(request.GET['saved_player'])
        user.save()
        return Response(user.saved_players, status=status.HTTP_204_NO_CONTENT)


        

def index(request):
    return render(request, 'players/index.html')



