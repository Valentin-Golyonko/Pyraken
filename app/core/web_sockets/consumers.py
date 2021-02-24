import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            chat_name = self.scope['url_route']['kwargs']['chat_name']
        except KeyError as ex:
            logger.error(f"connect(): {ex}")
            await self.close()
            return None
        else:
            if chat_name is None:
                logger.warning(f"connect(): chat_name is None.")
                await self.close()
                return None

        self.room_group_name = chat_name
        logger.debug(f"connect(): chat_name: {chat_name}")

        """ Join room group """
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        try:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
        except Exception as ex:
            logger.error(f"disconnect(): {ex}")
        else:
            # logger.debug(f"disconnect(): close_code: {close_code}")
            pass

    async def chat_message(self, event: dict):
        """ Receive message from room group """
        try:
            """ Send message to WebSocket """
            await self.send(text_data=json.dumps({
                'title': event.get('title'),
                'message': event.get('message'),
            }))
        except Exception as ex:
            logger.exception(f"chat_message(): {ex}")
        else:
            # logger.debug(f"chat_message(): event: {event}")
            pass
