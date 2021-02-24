from django.urls import re_path

from app.core.web_sockets.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<chat_name>\w+)/$', ChatConsumer.as_asgi()),
]
