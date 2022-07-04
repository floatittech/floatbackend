"""
Django settings for float project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uctz4=^(fhr!vj)5dm@)bcsg-$r!9@8nh^qpvn*p(+p*kr3cm^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', '.now.sh', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.postgres',
    "corsheaders",

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    'rest_framework',
    'rest_framework.authtoken',

    'floatapp.apps.FloatappConfig',
    'django_cleanup',
    'storages',
    'django_filters',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False

SITE_ID = 1
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'float-auth'
JWT_AUTH_REFRESH_COOKIE = 'float-refresh-token'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_AUTHENTICATION_CLASSES': ['dj_rest_auth.jwt_auth.JWTCookieAuthentication'],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'floatapp.serializers.CustomUserDetailsSerializer'
}

AUTH_USER_MODEL = 'floatapp.MyUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'float.urls'

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

WSGI_APPLICATION = 'float.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'float',
            'USER': 'postgres',
            'PASSWORD': '123456',
            'HOST': 'localhost',
            'PORT': '5433',
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=4),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]

CORS_EXPOSE_HEADERS = [
    'content-disposition',
    'responseType',
    ]
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # Contabo Server
# BUCKET_NAME = 'float'
# BUCKET_ENDPOINT_URL = 'https://sin1.contabostorage.com'
# #BUCKET_ENDPOINT_URL = 'https://api.vacancyjobalert.com/'
# BUCKET_REGION = ''

# # Contabo
# ACCESS_KEY='c5d4e71d002640ec8bbf162c73ed9c09'
# SECRET_KEY='25be48d8c8788f7621d5e013a93b3a5f'

# # S3 Server
# BUCKET_NAME = 'cdnaws.vacancyjobalert.com'
# AWS_S3_CUSTOM_DOMAIN = 'cdnaws.vacancyjobalert.com'
# BUCKET_REGION = 'ap-south-1'

# # S3 Server
# ACCESS_KEY='AKIAQMJZ5TPCVSO7LBXD'
# SECRET_KEY='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'

# Cloudflare R2 Server
BUCKET_NAME = 'awscdn'
BUCKET_ENDPOINT_URL = 'https://1df7b34158320f40e67a0fe217e4ce2c.r2.cloudflarestorage.com/'
#AWS_S3_CUSTOM_DOMAIN = 'cdncf.vacancyjobalert.com'
BUCKET_REGION = ''

# Cloudflare R2 Server
ACCESS_KEY='da28dda0fc93e0038e77a027f6a8d8ed'
SECRET_KEY='71b31c90307c6500ea7b1b69db61217c8f6801a8aae799380c45fb8215b6bccd'


# LINODE_BUCKET=os.environ.get('LINODE_BUCKET', 'cfe')
# LINODE_BUCKET_REGION=os.environ.get('LINODE_BUCKET_REGION',  'us-east-1')
# LINODE_BUCKET_ACCESS_KEY=os.environ.get('LINODE_BUCKET_ACCESS_KEY', 'GBN3RIQWFB4EAI8Y3SF7') 
# LINODE_BUCKET_SECRET_KEY=os.environ.get('LINODE_BUCKET_SECRET_KEY', 'S7zT9e5OSDeY4vwBBBm1BEdT8gFidE3qKkPNvwNB') 


AWS_S3_ENDPOINT_URL=BUCKET_ENDPOINT_URL
AWS_S3_ACCESS_KEY_ID=ACCESS_KEY
AWS_S3_SECRET_ACCESS_KEY=SECRET_KEY
AWS_S3_REGION_NAME=BUCKET_REGION
AWS_S3_USE_SSL=True
AWS_STORAGE_BUCKET_NAME=BUCKET_NAME
AWS_QUERYSTRING_EXPIRE='1800'

