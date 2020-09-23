from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Product, Cart
from .serializers import UserSerializer, ProductSerializer, CartSerializer
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'delete']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'delete']


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    http_method_names = ['post', 'delete']
