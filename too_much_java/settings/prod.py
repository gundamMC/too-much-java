import os

from too_much_java.settings.base import *


# Secret key - don't put your production secret key here
# https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/#secret-key
SECRET_KEY = os.environ['TMJ_SECRET_KEY']

DEBUG = False

# Allowed hosts
# A list of allowed domains
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-ALLOWED_HOSTS
ALLOWED_HOSTS = [
    'example.com',
    'www.example.com'
]

STATIC_ROOT = os.path.join(FRONTEND_DIR, 'dist')


# Database
# Again, like the secret key, don't put your password here 
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tmj_db',
        'USER': os.environ['TMJ_DB_USER'],
        'PASSWORD': os.environ['TMJ_DB_PASS'],
        'HOST': '127.0.0.1',
        'PORT': '23333',
    }
}