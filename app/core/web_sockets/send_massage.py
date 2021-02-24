import logging
import os
import sys

import django
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

""" for local usage -> """
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.expanduser(BASE_DIR)
if path not in sys.path:
    sys.path.insert(0, path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
""" <- for local usage """
logger = logging.getLogger(__name__)


class SendMassageWS:

    @classmethod
    def send_ws_msg(cls, chat_name: str, title: str, msg: str) -> None:
        try:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                chat_name,
                {
                    'type': 'chat.message',
                    'title': title,
                    'message': msg,
                }
            )
        except Exception as ex:
            logger.error(f"send_msg(): {ex}")

        return None


if __name__ == "__main__":
    SendMassageWS.send_ws_msg(
        chat_name='lobby',
        title='hello',
        msg='world'
    )
