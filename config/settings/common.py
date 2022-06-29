import os
from pathlib import Path

from dotenv import dotenv_values, load_dotenv

from app.core.constants.core_constants import CoreConstant

load_dotenv()

environ_values = {
    **dotenv_values(".env"),  # load sensitive variables
    **dotenv_values(".env_local"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # /<some_path>/Pyraken

SECRET_KEY = environ_values.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = environ_values.get('ALLOWED_HOSTS').split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_celery_beat',
    'django_extensions',
    'channels',

    'app.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

REDIS_USER = environ_values.get('REDIS_USER', '')
REDIS_PASS = environ_values.get('REDIS_PASS', '')

RABBIT_MQ_NAME = environ_values.get('RABBIT_MQ_NAME')
RABBIT_MQ_PASS = environ_values.get('RABBIT_MQ_PASS')
RABBIT_MQ_IP = environ_values.get('RABBIT_MQ_IP')
RABBIT_MQ_PORT = environ_values.get('RABBIT_MQ_PORT')

RUN_WITH_DOCKER = environ_values.get('RUN_WITH_DOCKER', 'false') == 'true'
if RUN_WITH_DOCKER:
    DB_HOST = "db"
    REDIS_HOST = f"redis://:{REDIS_PASS}@redis:6379"
    RABBIT_MQ_HOST = f"amqp://{RABBIT_MQ_NAME}:{RABBIT_MQ_PASS}@rabbitmq:{RABBIT_MQ_PORT}"
else:
    DB_HOST = environ_values.get('DB_HOST')
    REDIS_HOST = f"redis://:{REDIS_PASS}@127.0.0.1:6379"
    RABBIT_MQ_HOST = f"amqp://{RABBIT_MQ_NAME}:{RABBIT_MQ_PASS}@{RABBIT_MQ_IP}:{RABBIT_MQ_PORT}"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ_values.get('DB_NAME'),
        'USER': environ_values.get('DB_USER'),
        'PASSWORD': environ_values.get('DB_PASSWORD'),
        'HOST': DB_HOST,
        'PORT': environ_values.get('DB_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Celery settings ->
CELERY_BROKER_URL = RABBIT_MQ_HOST
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_TIMEZONE = TIME_ZONE

CELERY_DEFAULT_QUEUE = CoreConstant.DEFAULT_QUEUE
CELERY_DEFAULT_EXCHANGE = CoreConstant.DEFAULT_QUEUE
CELERY_DEFAULT_ROUTING_KEY = CoreConstant.DEFAULT_QUEUE

CELERY_IMPORTS = (
    'app.core.tasks',
)
CELERY_BEAT_SCHEDULE = {
    # xx:00 min
    # 'task-some-name': {
    #     'task': 'app.core.task_some_name',
    #     'schedule': crontab(hour='*', minute=0),
    # },
}
# <- Celery settings

# Django REST
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
#     'REFRESH_TOKEN_LIFETIME': timedelta(hours=3),
#     'UPDATE_LAST_LOGIN': True,
# }


# Django logging ->
DJANGO_LOG_LEVEL = 'WARNING'
APP_LOG_LVL = environ_values.get('APP_LOG_LVL', 'WARNING')
LOGS_DIR = 'logs/'
FILE_DJANGO = BASE_DIR / LOGS_DIR / 'django.log'
FILE_APPS_LOGS = BASE_DIR / LOGS_DIR / 'apps_logging.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} | {asctime} | {module} | {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} | {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file_django': {
            'level': DJANGO_LOG_LEVEL,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 30,
            'filename': FILE_DJANGO,
            'formatter': 'verbose',
        },
        'file': {
            'level': APP_LOG_LVL,
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 30,
            'filename': FILE_APPS_LOGS,
            'formatter': 'verbose',
        },
        'console': {
            'level': APP_LOG_LVL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ('file_django', 'console'),
            'level': DJANGO_LOG_LEVEL,
            'propagate': True,
        },
        # apps logging
        'app.core': {
            'handlers': ('file', 'console'),
            'level': APP_LOG_LVL,
            'propagate': True,
        },
        # other
        'config.queues_scripts': {
            'handlers': ('file', 'console'),
            'level': APP_LOG_LVL,
            'propagate': True,
        },
    },
}
# <- Django logging

# Send email Google
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587  # 587 for TLS, 465 for SSL

# Web Sockets ->
ASGI_APPLICATION = "config.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [REDIS_HOST],
        },
    },
}
# <- Web Sockets

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
