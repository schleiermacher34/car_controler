"""
URL configuration for car_control project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from car import views

urlpatterns = [
    path('', include('your_app.urls')),
    path('move_forward/', views.move_forward, name='move_forward'),
    path('move_backward/', views.move_backward, name='move_backward'),
    path('turn_left/', views.turn_left, name='turn_left'),
    path('turn_right/', views.turn_right, name='turn_right'),
    path('stop/', views.stop_car, name='stop_car'),
]


