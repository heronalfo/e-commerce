from env import DEBUG
from env import ALLOWED_HOSTS

ROOT_URLCONF = 'config.urls'

INTERNAL_IPS = [ "127.0.0.1", ]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

WSGI_APPLICATION = 'config.wsgi.application'