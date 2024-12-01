from django.urls import path
from . import views

urlpatterns = [
    path('api/get_command/', views.get_command, name='get_command'),
    path('send_command/', views.send_command, name='send_command'),
]
