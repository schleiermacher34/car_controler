import requests
from django.http import JsonResponse
from django.shortcuts import render

# Replace with your ESP32's IP address
ESP32_IP = 'http://192.168.1.100'  # Example IP (use your ESP32 IP)
ESP32_CONTROL_PATH = '/control'    # Assume the endpoint on the ESP32

# Function to send command to the ESP32
def send_car_command(command):
    try:
        response = requests.post(f'{ESP32_IP}{ESP32_CONTROL_PATH}', data={'command': command})
        return response.json()  # ESP32 returns status in JSON
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

# Views for car control actions
def move_forward(request):
    result = send_car_command('move_forward')
    return JsonResponse(result)

def move_backward(request):
    result = send_car_command('move_backward')
    return JsonResponse(result)

def turn_left(request):
    result = send_car_command('turn_left')
    return JsonResponse(result)

def turn_right(request):
    result = send_car_command('turn_right')
    return JsonResponse(result)

def stop_car(request):
    result = send_car_command('stop')
    return JsonResponse(result)

# Index page for control panel
def index(request):
    return render(request, 'car_control.html')  # This is your control panel page
