from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from .models import Player, SavedPlayers
from .serializers import PlayerSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['GET', 'POST', 'DELETE'])
# The api retrives or creates the player when get is called, update the player name when post is called, also deletes the player when delete is called.
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
# The api retreves all players when get is called, creates a new player when post is called, and deletes all players when delete is called.
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
@permission_classes([IsAuthenticated])
def SavedPlayers(request):
    try:
        if request.method == 'GET':
            saved_players = SavedPlayers.objects.get(user=request.user)
            return Response(saved_players.saved_players)
        elif request.method == 'POST':
            saved_players = SavedPlayers.objects.get(user=request.user)
            saved_players.saved_players.append(request.data['summoner_name'])
            saved_players.save()
            return Response(saved_players.saved_players)
        elif request.method == 'DELETE':
            saved_players = SavedPlayers.objects.get(user=request.user)
            saved_players.saved_players.remove(request.data['summoner_name'])
            saved_players.save()
            return Response(saved_players.saved_players)
    except:
        raise Http404


# Token authentication
@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user(request):
    if request.user.is_authenticated:
        return Response(request.user.username)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)



# cadastra um novo usuario, recebendo o username e a senha
@api_view(['POST'])
def register(request):
    username = request.data['username']
    password = request.data['password']
    user = Player.objects.create_user(username, password)
    user.save()
    return Response(status=status.HTTP_201_CREATED)

# verifica se o usuario ja existe
@api_view(['GET'])
def check_user(request):
    try:
        user = Player.objects.get(username=request.GET['username'])
        return Response(status=status.HTTP_208_ALREADY_REPORTED)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_200_OK)





        

def index(request):
    return render(request, 'players/index.html')



