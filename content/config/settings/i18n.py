from django.utils.translation import gettext_lazy as _
from .base_dir import BASE_DIR
from os.path import join

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGES = [
    ('en', _('English')),
    ('pt', _('Portuguese')),   
]

# Translation storage location
LOCALE_PATHS = [
    join(BASE_DIR, 'locale'),
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True