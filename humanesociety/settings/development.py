from .base import *
from .base import _

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'project.db',
    }
}
DEBUG = True
TEMPLATE_DEBUG = DEBUG
MEDIA_URL = 'http://localhost:9966/media/'
MEDIA_ROOT = _('media')
STATIC_ROOT = _('public')
SECRET_KEY = 'the coolest of cool stories, bro'
INSTALLED_APPS = list(INSTALLED_APPS) + [
    'django.contrib.webdesign'
]
