"""
List of available ENVs:
- ENGINE_SECRET_KEY=
- ENGINE_DEBUG=True
- ENGINE_ALLOWED_HOSTS=example.com,anothersite.com
- ENGINE_DATABASE_NAME=
- ENGINE_DATABASE_USER=
- ENGINE_DATABASE_PASSWORD=
- ENGINE_DATABASE_HOST=
- ENGINE_DATABASE_PORT=
- ENGINE_DATABASE_ATOMIC_REQUESTS=
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('ENGINE_SECRET_KEY', 'django-insecure-jxnfgj%r)grl&ljxr#u+x+1l&&3*w*riq2pv+_@=oo-re6bzbr')  # noqa: E501
DEBUG = os.getenv('ENGINE_DEBUG', "True").lower() == "true"
ALLOWED_HOSTS = os.getenv('ENGINE_ALLOWED_HOSTS', ",").split(',')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'pugs',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('ENGINE_DATABASE_NAME'),
        'USER': os.getenv('ENGINE_DATABASE_USER'),
        'PASSWORD': os.getenv('ENGINE_DATABASE_PASSWORD'),
        'HOST': os.getenv('ENGINE_DATABASE_HOST'),
        'PORT': os.getenv('ENGINE_DATABASE_PORT', 5432),
        'ATOMIC_REQUESTS': os.getenv('ENGINE_DATABASE_ATOMIC_REQUESTS', "True").lower() == "true"
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kuala_Lumpur'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
