"""
Django settings for hisse_project project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/



# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '86)5)oyuk%++vbcyba*1pty1dwkl_p!!*su^&^q8_*-18-qvr1'
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['enigmatic-sierra-45569.herokuapp.com','.herokuapp.com', 'localhost', '127.0.0.1']


ENVIRONMENT = os.environ.get('ENVIRONMENT', default='development')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # new
    'django.contrib.staticfiles',
    'django.contrib.sites', # new

     # Third-party
    'crispy_forms', # new
    'allauth', # new
    'allauth.account', # new


    # Local
    'users.apps.UsersConfig', # new
    'pages.apps.PagesConfig', # new
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # new
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hisse_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # new
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

WSGI_APPLICATION = 'hisse_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),] # new
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # new
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

AUTH_USER_MODEL = 'users.CustomUser' # new

# django-allauth config
LOGIN_REDIRECT_URL = 'home' # new
#LOGOUT_REDIRECT_URL = 'home' # new
ACCOUNT_LOGOUT_REDIRECT = 'home' # new

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4' # new


# django-allauth config
SITE_ID = 1 # new


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend', # new
)


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # new

ACCOUNT_SESSION_REMEMBER = True # new

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True # no need but just to see..

#for email only login:
ACCOUNT_USERNAME_REQUIRED = False # new
ACCOUNT_AUTHENTICATION_METHOD = 'email' # new
ACCOUNT_EMAIL_REQUIRED = True # new
ACCOUNT_UNIQUE_EMAIL = True # new


# production
if ENVIRONMENT == 'production':
    SECURE_BROWSER_XSS_FILTER = True # new
    X_FRAME_OPTIONS = 'DENY' # new
    SECURE_SSL_REDIRECT = True # new
    SECURE_HSTS_SECONDS = 3600 # new
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True # new
    SECURE_HSTS_PRELOAD = True # new
    SECURE_CONTENT_TYPE_NOSNIFF = True # new
    SESSION_COOKIE_SECURE = True # new
    CSRF_COOKIE_SECURE = True # new
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # new


# Heroku
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
