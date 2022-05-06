from channels.generic.websocket import AsyncWebsocketConsumer
import json

class CryptoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('data_update', self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard('data_update', self.channel_name)

    async def update_data(self, event):
        data = event['text']
        await self.send(text_data=json.dumps(data))