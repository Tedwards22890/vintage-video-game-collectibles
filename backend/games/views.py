from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Game
from .serializers import GamesSerializer

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
def game_list(request):
    games = Game.objects.all()
    serializer = GamesSerializer(games, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_games(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = GamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        games = Game.objects.filter(user_id=request.user.id)
        serializer = GamesSerializer(games, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def games_by_id(request, game_id):
    games =Game.objects.filter(game_id=request.game.id)
    serializer = GamesSerializer(games, many=True)
    return Response(serializer.data)