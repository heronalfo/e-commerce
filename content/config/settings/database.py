from .base_dir import BASE_DIR
from env import DJANGO

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASE = DJANGO['DATABASE']
DATABASES = {
    'default': {
        'ENGINE': DATABASE['ENGINE'],
        
        'NAME': DATABASE['NAME'],
        'USER': DATABASE['USER'],
        'PASSWORD': DATABASE['PASSWORD'],
        'HOST': DATABASE['HOST'],
        'PORT': DATABASE['PORT'],

    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'