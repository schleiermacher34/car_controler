from django.urls import path
from car.consumers import CarControlConsumer

websocket_urlpatterns = [
    path("ws/car_control/", CarControlConsumer.as_asgi()),
]
