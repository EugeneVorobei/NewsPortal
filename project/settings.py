"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tyjp(le4o&!@8^qu$^m!9-h56e^emsrxmlo#k9sbil&7cgkbo&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_extensions',
    'django_filters',
    'django_apscheduler',
    'simpleapp.apps.SimpleappConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'sign',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'sign.models.CommonSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'EvgeniVorobey'
EMAIL_HOST_PASSWORD = '12wsxCDE#$'
EMAIL_USE_SSL = True

ADMINS = [
    ('Name', 'mail@mail.com'),
]

SERVER_EMAIL = 'EvgeniVorobey@yandex.ru'  # ?????????? ??????????????????????

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@yandex.ru' # ???????? ???? ?????????????????????? ????????????, ???? ???? ???????????????? ???????????????? + ???@yandex.ru???

# ???????????? ????????, ?????????????? ?????????? ???????????????????????? ?????? ???????????????? (???????????????????? ???????????? ???? ????????????????)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# ???????? ???????????? ???? ?????????????????????? ???? 25 ????????????, ???? ?????? ?????????????????????????? ??????????????????, ???????????? ?????????????????? ?????????? ????????????????, ???? ?????? ??????????????, ?????? ???????????? ???????? ???? ???????????????????????????????????? ??????????????
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds


CELERY_BROKER_URL = 'redis://:YTrPmvwBkRWASfCKBZoSEGfEYpIwQrYk@redis-17306.c89.us-east-1-3.ec2.cloud.redislabs.com:17306/0'
CELERY_RESULT_BACKEND = 'redis://:YTrPmvwBkRWASfCKBZoSEGfEYpIwQrYk@redis-17306.c89.us-east-1-3.ec2.cloud.redislabs.com:17306/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # ??????????????????, ???????? ?????????? ?????????????????? ???????????????????? ??????????! ???? ???????????????? ?????????????? ?????????? cache_files ???????????? ?????????? ?? manage.py!
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'debug_format': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'warning_format': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'error_format': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'general.log_format': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'errors.log_format': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'security.log_format': {
            'format': '%(asctime)s %(levelname)s $(module)s %(message)s'
        },
        'send_email_format': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'debug_handler': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'debug_format'
        },
        'warning_handler': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'warning_format'
        },
        'error_handler': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error_format'
        },
        'general.log_handler': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': './logs/general.log',
            'formatter': 'general.log_format'
        },
        'errors.log_handler': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': './logs/errors.log',
            'formatter': 'errors.log_format'
        },
        'security.log_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './logs/security.log',
            'formatter': 'security.log_format'
        },
        'mail_admins_handler': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'formatter': 'send_email_format',
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['debug_handler', 'warning_handler', 'error_handler', 'general.log_handler'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors.log_handler', 'mail_admins_handler'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['errors.log_handler', 'mail_admins_handler'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['errors.log_handler'],
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['errors.log_handler'],
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security.log_handler'],
            'propagate': True,
        }
    }
}
