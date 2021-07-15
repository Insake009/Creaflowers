from django.urls import path
from .views import FlowerAPIView


urlpatterns = [
    # path('contact/<int:pk>/', ContactAPIView.as_view()),
    path('',FlowerAPIView.as_view())
]