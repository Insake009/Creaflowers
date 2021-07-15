from rest_framework import serializers
from .models import GoodsOrder,Order,FlowerOrder

class GoodsOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsOrder
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class FlowerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowerOrder
        fields = '__all__'