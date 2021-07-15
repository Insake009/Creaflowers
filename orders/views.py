from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import OrderSerializer,GoodsOrderSerializer,FlowerOrderSerializer

class OrderCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class GoodsOrderCreateAPIView(generics.ListCreateAPIView):
    queryset = GoodsOrder.objects.all()
    serializer_class = GoodsOrderSerializer

class FlowerOrderCreateAPIView(generics.ListCreateAPIView):
    queryset = FlowerOrder.objects.all()
    serializer_class = FlowerOrderSerializer
