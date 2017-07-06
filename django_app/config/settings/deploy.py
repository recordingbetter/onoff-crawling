from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# AWS settings
AWS_ACCESS_KEY_ID = config_secret_deploy['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_deploy['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_deploy['aws']['s3_bucket_name']
S3_USER_SIGV4 = True

# Storage settings
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'


# Static URLs
STATIC_URL = '/static/'
# 프로젝트 내부에 저장하지 않고 AWS s3에 저장할거라 필요없음
# STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')

# Media URLs
MEDIA_URL = '/media/'
# 프로젝트 내부에 저장하지 않고 AWS s3에 저장할거라 필요없음
# MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')

DEBUG = True
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = config_secret_deploy['django']['database']

SECRET_KEY = config_secret_common['django']['secret_key']

# print('@@@@@@@ DEBUG:', DEBUG)
# print('@@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)
