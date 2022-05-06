from django.urls import path
from .consumers import CryptoConsumer

ws_urlpatterns = [
    path('ws/update/', CryptoConsumer.as_asgi()),
]