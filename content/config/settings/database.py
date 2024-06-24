from .base_dir import BASE_DIR
from env import DATABASE_NAME

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        
        'NAME': BASE_DIR / DATABASE_NAME,

    }
}