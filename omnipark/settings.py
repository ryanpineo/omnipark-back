import os

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6vvl31l*slr&!qij#*pk*kx0f1ys1v@a1k9==&lhs=-(o1agv5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Auth
AUTH_USER_MODEL = 'users.User'

# Application definition

INSTALLED_APPS = [
    'omnipark.api.apps.ApiConfig',
    'omnipark.merchants.apps.MerchantsConfig',
    'omnipark.parking.apps.ParkingConfig',
    'omnipark.users.apps.UsersConfig',

    'rest_framework',
    'rest_framework.authtoken',
    'push_notifications',
    'nested_admin',
    'fsm_admin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
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

ROOT_URLCONF = 'omnipark.urls'

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

WSGI_APPLICATION = 'omnipark.wsgi.application'


# Database
DATABASES = {
    'default': dj_database_url.parse('postgis://ryan:@localhost/omnipark'),
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    'ORDERING_PARAM': 'order_by',
    'SEARCH_PARAM': 'q',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

# Push Notifications
PUSH_NOTIFICATIONS_SETTINGS = {
        "APNS_CERTIFICATE": "/home/ryan/projects/tsl/hackathons/2017-money2020/apns.pem",
        "APNS_TOPIC": "com.silverlogic.OmniPark",
}

# Visa
VISA_CERT = '/home/ryan/projects/tsl/hackathons/2017-money2020/cert.pem'
VISA_PRIVKEY = '/home/ryan/projects/tsl/hackathons/2017-money2020/key_65f7f255-9b15-4492-9c66-12d46ebd63cd.pem'
VISA_USERNAME = os.environ['VISA_USERNAME']
VISA_PASSWORD = os.environ['VISA_PASSWORD']
