import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CarControlConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Handle the data received
        command = data.get('command')
        print(f"Received command: {command}")

        # Respond to ESP32
        await self.send(text_data=json.dumps({
            'message': f"Command {command} received"
        }))
