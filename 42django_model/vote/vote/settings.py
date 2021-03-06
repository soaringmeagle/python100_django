"""
Django settings for vote project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '69esyju@a*4yibw^w+x--i5(9clb7&v+)#esa+dyo+9q_x46nc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'debug_toolbar',
    'polls',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'vote.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'vote.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vote',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'CHARSET': 'utf8',
        'TIME_ZONE': 'Asia/Shanghai',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# ???????????????????????????URL??????
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# LOGGING = {
#     'version': 1,
#     # ????????????????????????????????????
#     'disable_existing_loggers': False,
#     # ??????????????????
#     'formatters': {
#         'simple': {
#             'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
#             'datefmt': '%Y-%m-%d %H:%M:%S',
#         },
#         'verbose': {
#             'format': '%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
#                       '%(module)s.%(funcName)s line %(lineno)d: %(message)s',
#             'datefmt': '%Y-%m-%d %H:%M:%S',
#         }
#     },
#     # ???????????????
#     'filters': {
#         # ?????????Django???????????????DEBUG??????True???????????????
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     # ???????????????
#     'handlers': {
#         # ??????????????????
#         'console': {
#             'class': 'logging.StreamHandler',
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'formatter': 'simple',
#         },
#         # ???????????????(??????????????????)
#         'file1': {
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': 'access.log',
#             'when': 'W0',
#             'backupCount': 12,
#             'formatter': 'simple',
#             'level': 'INFO',
#         },
#         # ???????????????(??????????????????)
#         'file2': {
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': 'info.log',
#             'when': 'D',
#             'backupCount': 31,
#             'formatter': 'verbose',
#             'level': 'INFO',
#         },
#     },
#     # ??????????????????
#     'loggers': {
#         'django': {
#             # ??????????????????????????????
#             'handlers': ['file2'],
#             # ??????????????????????????????
#             'propagate': True,
#             # ????????????(?????????????????????????????????)
#             'level': 'DEBUG',
#         },
#     }
# }
# debug_toolbar??????
DEBUG_TOOLBAR_CONFIG = {
    # ??????jQuery???
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
    # ?????????????????????
    'SHOW_COLLAPSED': True,
    # ?????????????????????
    'SHOW_TOOLBAR_CALLBACK': lambda x: True,
}


# ?????????????????????????????????????????????
REST_FRAMEWORK = {
    # ????????????????????????
    # 'PAGE_SIZE': 10,
    # ????????????????????????
    # 'DEFAULT_PAGINATION_CLASS': '...',
    # ?????????????????????
    # 'EXCEPTION_HANDLER': '...',
    # ?????????????????????
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    #     'rest_framework.parsers.FormParser',
    #     'rest_framework.parsers.MultiPartParser',
    # ),
    # ?????????????????????
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     '...'
    # ),
    # ?????????????????????
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     '...',
    # ),
    # ?????????????????????
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     '...',
    # ),
}

# django-redis??????
CACHES = {
        'default': {
            # ????????????django-redis??????Redis??????
            'BACKEND': 'django_redis.cache.RedisCache',
            # Redis????????????URL
            'LOCATION': ['redis://127.0.0.1:6379/0', ],
            # Redis???????????????????????????????????????
            'KEY_PREFIX': 'vote',
            # ?????????????????????
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                # ?????????????????????????????????Redis???????????????
                'CONNECTION_POOL_KWARGS': {
                    # ???????????????
                    'max_connections': 512,
                },
                # ??????Redis???????????????
                # 'PASSWORD': 'foobared',
            }
        },
    }