"""
!!! ONLY FOR LOCAL (DEV) RUN !!!
"""
from config.settings.common import *

DEBUG = True

ALLOWED_HOSTS.extend(("127.0.0.1", "localhost"))

if not RUN_WITH_DOCKER:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': environ_values.get('DB_NAME', ''),
            'USER': environ_values.get('DB_USER', ''),
            'PASSWORD': environ_values.get('DB_PASSWORD', ''),
            'HOST': DB_HOST,
            'PORT': environ_values.get('DB_PORT', ''),
            'TEST': {
                'NAME': 'test_db',  # coverage run --source='./app' manage.py test app --keepdb
            },
        }
    }

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0  # 3600 sec = 1h, 31536000 sec = 1 year

# if DEBUG:
#     INTERNAL_IPS = (
#         "127.0.0.1",
#     )
#
#     DEBUG_TOOLBAR_PANELS = (
#         'debug_toolbar.panels.history.HistoryPanel',
#         'debug_toolbar.panels.versions.VersionsPanel',
#         'debug_toolbar.panels.timer.TimerPanel',
#         'debug_toolbar.panels.settings.SettingsPanel',
#         'debug_toolbar.panels.headers.HeadersPanel',
#         'debug_toolbar.panels.request.RequestPanel',
#         # 'debug_toolbar.panels.sql.SQLPanel',  # !
#         'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#         'debug_toolbar.panels.templates.TemplatesPanel',
#         'debug_toolbar.panels.cache.CachePanel',
#         'debug_toolbar.panels.signals.SignalsPanel',
#         'debug_toolbar.panels.logging.LoggingPanel',
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#         'debug_toolbar.panels.profiling.ProfilingPanel',
#     )
#
#     INSTALLED_APPS = ('debug_toolbar', *INSTALLED_APPS)
#     MIDDLEWARE = (*MIDDLEWARE, 'debug_toolbar.middleware.DebugToolbarMiddleware')
