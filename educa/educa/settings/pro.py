from .base import *

DEBUG = False

ADMINS = (
    ('cosmo', 'marcjohnson518@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'cosmo',
       'USER': 'cosmo',
       'PASSWORD': '******',
   }
}

# SSL config
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
