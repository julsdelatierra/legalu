import os

PRODUCT_NAME = 'Legal'
PRODUCT_DESCRIPTION = 'Documentos legales rapido y facil.'
COMPANY = 'iWantoo Inc.'

PROJECT_DIR = os.path.abspath(os.path.dirname('__file__'))
URL = 'http://localhost:8000'

path = lambda *args: os.path.join(PROJECT_DIR, *args)

DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('admin', 'mail@company.com'),
)

MANAGERS = ADMINS


AUTH_PROFILE_MODULE = 'auth.UserProfile'

LOGIN_REDIRECT_URL = '/home/'
LOGIN_URL = '/'

# Twitter keys
TWITTERAUTH_KEY = ''
TWITTERAUTH_SECRET = ''

# Facebook keys
APP_ID_FACEBOOK = ''
SECRET_KEY_FACEBOOK = ''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path('db.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = path('media')

MEDIA_URL = URL+'/medios'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'iiybage0^@igkdua+wxk%+jcm*e_po2$8n9$-5h2!2^1#6*3s+'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'legal.urls'

TEMPLATE_DIRS = (
    path('auth','templates'),
    path('main','templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'auth',
    'main',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    'context_processors.default',
)
