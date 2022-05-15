"""
!!! ONLY FOR LOCAL (DEV) RUN !!!
"""
from dotenv import dotenv_values, load_dotenv

from config.settings.common import *

load_dotenv()

environ_values = {
    **dotenv_values(".env"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

SECRET_KEY = environ_values.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = environ_values.get('ALLOWED_HOSTS').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ_values.get('DB_NAME', ''),
        'USER': environ_values.get('DB_USER', ''),
        'PASSWORD': environ_values.get('DB_PASSWORD', ''),
        'HOST': '127.0.0.1',  # os.environ.get('DB_HOST', ''),
        'PORT': environ_values.get('DB_PORT', ''),
    }
}

RABBIT_MQ_NAME = environ_values.get('RABBIT_MQ_NAME')
RABBIT_MQ_PASS = environ_values.get('RABBIT_MQ_PASS')
RABBIT_MQ_IP = environ_values.get('RABBIT_MQ_IP')
RABBIT_MQ_PORT = environ_values.get('RABBIT_MQ_PORT')

CELERY_BROKER_URL = f"amqp://{RABBIT_MQ_NAME}:{RABBIT_MQ_PASS}@{RABBIT_MQ_IP}:{RABBIT_MQ_PORT}"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
