"""
Django settings for blogapi project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import json, sys, os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#ROOT_DIR = BASE_DIR.parent
#SECRET_BASE_FILE = os.path.join(ROOT_DIR, 'secrets.json')
ROOT_DIR = os.path.dirname(BASE_DIR)
SECRET_BASE_FILE = os.path.join(ROOT_DIR, 'blogapi/secrets.json')
secrets = json.loads(open(SECRET_BASE_FILE).read())
for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG', 'True') != 'False')

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    #'rest_auth',
    #'rest_auth.registration',
    'allauth',
    'allauth.account',
    'django.contrib.sites',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    #'djangorestframeworksimplejwt',    
    'home',

    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SITE_ID = 1

AUTH_USER_MODEL = 'accounts.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogapi.urls'

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

WSGI_APPLICATION = 'blogapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_USE_JWT = True

ACCOUNT_EMAIL_VERIFICATION = 'none'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}



SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


AWS_ACCESS_KEY_ID = 'AKIATKPN7RBSGBUOBXOQ'
AWS_SECRET_ACCESS_KEY ='django-insecure-_v06y+lk!pa7^$xwp)-vs*@-@l0#usm@r-__%p+y1k%c%n(bfz'
AWS_STORAGE_BUCKET_NAME = 'aws10thcho'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'ap-northeast-2'