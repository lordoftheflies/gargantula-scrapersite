import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.execution_id = self.scope['url_route']['kwargs']['execution_id']
        self.execution_group_name = 'execution_%s' % self.execution_id

        # Join room group
        await self.channel_layer.group_add(
            self.execution_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.execution_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive_json(self, content):
        # text_data_json = json.loads(text_data)
        message = content['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.execution_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send_json(content=message)


class ProcessConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.process_id = self.scope['url_route']['kwargs']['process_id']
        self.process_group_name = 'process_%s' % self.process_id
        # self.group_name = 'status'
        # Join room group
        await self.channel_layer.group_add(
            self.process_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.process_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive_json(self, content, **kwargs):
        # text_data_json = json.loads(text_data)
        message = content['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.process_group_name,
            dict(type='publish_state', message=message)
        )

    # Receive message from room group
    async def publish_state(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send_json(content=message)
