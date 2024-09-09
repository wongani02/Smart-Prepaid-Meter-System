from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    path('ws/balance/<int:meter_number>/', consumers.PrepaidBalanceConsumer.as_asgi()),
]