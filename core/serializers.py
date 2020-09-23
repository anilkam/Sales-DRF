from rest_framework import serializers
from .models import Product, Cart
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity']


class CartListSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = Cart
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity', 'sub_total']        


class UserSerializer(serializers.ModelSerializer):
    cart_set = CartListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'cart_set']
