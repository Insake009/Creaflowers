from django.urls import path
from rest_framework import routers
# from .views import ContactViewSet
from .views import ContactAPIView

# router = routers.SimpleRouter()
# router.register('contact', ContactViewSet)
# urlpatterns = router.urls

urlpatterns = [
    path('contact/<int:pk>/', ContactAPIView.as_view()),
]