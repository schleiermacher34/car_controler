import requests
from django.http import JsonResponse
from django.shortcuts import render

# Replace with your ESP32's IP address
ESP32_IP = 'http://192.168.1.100'  # Example IP (use your ESP32 IP)
ESP32_CONTROL_PATH = '/control'    # Assume the endpoint on the ESP32

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Command
from .serializers import CommandSerializer
from django.shortcuts import render, redirect

@api_view(['GET'])
def get_command(request):
    command = Command.objects.filter(executed=False).order_by('-timestamp').first()
    if command:
        serializer = CommandSerializer(command)
        # Mark command as executed
        command.executed = True
        command.save()
        return Response(serializer.data)
    else:
        return Response({'command': 'none'})





def send_command(request):
    if request.method == 'POST':
        command = request.POST.get('command')
        Command.objects.create(command=command)
        return redirect('send_command')
    return render(request, 'send_command.html')


# Index page for control panel
def index(request):
    return render(request, 'car_control.html')  # This is your control panel page
