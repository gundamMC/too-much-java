from .base import *


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

STATICFILES_DIRS = (
    os.path.join(FRONTEND_DIR, 'dist'),
    # frontend files
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Database
# Again, like the secret key, don't put your password here 
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tmj',
        'USER': os.environ['TMJ_DB_USER'],
        'PASSWORD': os.environ['TMJ_DB_PASS'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
