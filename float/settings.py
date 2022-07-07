from email.policy import default
import dj_database_url
from decouple import config
from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

## SECRET_KEY
SECRET_KEY = config('DJANGO_SECRET_KEY')

##Debug
DEBUG = config('DEBUG', cast=bool)

## Allowed Hosts
ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

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
    'whitenoise.middleware.WhiteNoiseMiddleware',  # White Noise For Satic Files
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware", # CORS Header
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
DATABASES = {
    'default': dj_database_url.config('DATABASE_URL', default=config('DATABASE_URL'), conn_max_age=600)
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

## JWT Details
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=config('ACCESS_TOKEN_LIFETIME', default=4, cast=int)),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=config('REFRESH_TOKEN_LIFETIME', default=2, cast=int)),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}
#CORS Headers
CORS_ALLOWED_ORIGINS = [config('CORS_ALLOWED')]

CORS_EXPOSE_HEADERS = [
    'content-disposition',
    'responseType',
    ]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

## S3 Storage
AWS_S3_ENDPOINT_URL = config('S3_BUCKET_ENDPOINT_URL')
AWS_S3_ACCESS_KEY_ID = config('S3_ACCESS_KEY')
AWS_S3_SECRET_ACCESS_KEY = config('S3_SECRET_KEY')
AWS_S3_REGION_NAME = config('S3_BUCKET_REGION')
AWS_S3_USE_SSL=True
AWS_STORAGE_BUCKET_NAME = config('S3_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = config('S3_CUSTOM_DOMAIN')
AWS_QUERYSTRING_EXPIRE=config('S3_QUERYSTRING_EXPIRE_TIME', default='1800')