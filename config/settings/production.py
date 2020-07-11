# Python imports
import os

# Project imports
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SET ALLOWED HOSTS
ALLOWED_HOSTS = ['yttags.com', 'www.yttags.com']

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USERNAME'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    },
}

# SMTP
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['EMAIL_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']
ADMIN_EMAIL_ADDRESS = os.environ['ADMIN_EMAIL']

# YouTube Auth Key
YOUTUBE_KEY = os.environ['YOUTUBE_KEY']

# Sentry configuration
sentry_sdk.init(
    dsn=os.environ['SENTRY_DSN'],
    integrations=[DjangoIntegration()],
    send_default_pii=True
)
