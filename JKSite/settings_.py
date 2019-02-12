"""
Django settings for JKSite project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'HASKERS DONT LOOK'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
USE_SIDE_DB = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'jediknightchannel.duckdns.org',
    'jediknightchannel.ru',
    'jediknightchannel.tk',
    '176.57.71.131',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_hosts',
    'social_django',
    'smuggler',
    'rest_framework',
    'el_pagination',
    'api',
    'main',
    'news',
    'translation',
    'video',

]

MIDDLEWARE = [
    #'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django_hosts.middleware.HostsResponseMiddleware'
]

ROOT_URLCONF = 'JKSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.template.context_processors.request',
            ],
        },
    },
]


WSGI_APPLICATION = 'JKSite.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'JKSitelogfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'JKSite.log'),
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 10,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'JKSite': {
            'handlers': ['JKSitelogfile', ],
            'level': 'DEBUG',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


GOOGLE_RECAPTCHA_SECRET_KEY = 'DONT LOOK'

#DEFAULT_HOST = 'jediknightchannel.ru'
#ROOT_HOSTCONF = 'JKSite.hosts'

SOCIAL_NETWORKS_APPLICATION_IDS = {'vk': 'a', 'yandex': 'b'}
SOCIAL_NETWORKS_APPLICATION_PASSWORDS = {'vk': 'a', 'yandex': 'b'}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.yahoo.YahooOpenId',
    'social_core.backends.yandex.YandexOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_YANDEX_OAUTH2_KEY = 'c'
SOCIAL_AUTH_YANDEX_OAUTH2_SECRET = 'c'

PJS_BASE64_SEPARATOR = b"separatist"
PJS_BASE64_KEYS = ["1", "2", "3", "4", "5"]


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
side_db = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'JKSite',
            'USER': 'user',
            'PASSWORD': 'pwd',
            'HOST': 'a',
            'PORT': '3306',
            'OPTIONS': {'charset': 'utf8mb4'},
        }
    }
main_db = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'JKSite',
            'USER': 'user',
            'PASSWORD': 'pwd',
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {'charset': 'utf8mb4'},
        }
    }


if USE_SIDE_DB:
    DATABASES = side_db
else:
    DATABASES = main_db

if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static/'),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')