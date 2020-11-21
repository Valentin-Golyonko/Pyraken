from datetime import timedelta

from config.settings.common import *

SECRET_KEY = '123'

DEBUG = True

ALLOWED_HOSTS = ['*']

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
