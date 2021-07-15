from django.urls import path
from .views import OrderCreateAPIView, FlowerOrderCreateAPIView,GoodsOrderCreateAPIView


urlpatterns = [
    path('order/',OrderCreateAPIView.as_view()),
    path('order/flowerorder/',FlowerOrderCreateAPIView.as_view()),
    path('order/goodorder/',GoodsOrderCreateAPIView.as_view())
]