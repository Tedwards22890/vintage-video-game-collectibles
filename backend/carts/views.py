from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Cart
from .serializers import CartSerializer

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_carts(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def cart_by_id(request, pk):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    cart = get_object_or_404(Cart, pk=pk)
    if request.method == 'GET':
        cart = Cart.objects.filter(user_id=request.user.id)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cart_post(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)