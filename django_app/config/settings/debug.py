from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.debug.application'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')

# Media URLs
MEDIA_URL = '/media/'
# django_app/media
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')

# INSTALLED APPS
INSTALLED_APPS.append('django_extensions')

# 디버그모드니까 DEBUG는 True
DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

print('@@@@@@@ DEBUG:', DEBUG)
print('@@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)
