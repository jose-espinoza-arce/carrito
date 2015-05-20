"""
Django settings for maravatio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.utils.translation import ugettext_lazy as _

os.environ["LANGUAGE"] = 'es_MX'

# Oscar's imports
from oscar import get_core_apps, OSCAR_MAIN_TEMPLATE_DIR
from oscar.defaults import *
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    OSCAR_MAIN_TEMPLATE_DIR,
)
#OSCAR_MAIN_TEMPLATE_DIR = os.path.join(BASE_DIR,
#                                       '..',
#                                       'carritoenv', 'local',
#                                       'lib', 'python2.7',
#                                       'site-packages', 'oscar',
#                                       'templates', 'oscar',
#                                       )
    #'/home/jose/dev/djangodev/carrito/carritoenv/local/lib/python2.7/site-packages/oscar/templates/oscar'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p(pdpb$wjlzi=axdiko(%x$@r=+ik-d&v+u$x14-es-)!tg)cy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'compressor',
    'widget_tweaks',
    'paypal',
    'cmproducts',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken'
] + get_core_apps()

SITE_ID = 1


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz"
    'django.contrib.messages.context_processors.messages',

    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]


#Cors settings
CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITE_LIST = (
    'google.com',
)

#RESTFRAMEWORK settings
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

#Oscar Settings
#PAYPAL_API_USERNAME = 'backend2.muchaweb-facilitator_api1.gmail.com'
#PAYPAL_API_PASSWORD = '4UPPDRXCPHJRRY5C'
#PAYPAL_API_SIGNATURE = 'AiPC9BjkCyDFQXbSkoZcgqH3hpacAhdkOcwnyfie6A21NvoIfMCOcR.L'

PAYPAL_PAYFLOW_VENDOR_ID = 'RH3VFB4DGXFYW'

PAYPAL_PAYFLOW_PASSWORD = 'Back2014'

PAYPAL_CURRENCY = 'MXN'

OSCAR_DEFAULT_CURRENCY = 'MXN'

#OSCAR_DASHBOARD_NAVIGATION.append(
#    {
#        'label': _('PayPal'),
#        'icon': 'icon-globe',
#        'children': [
#            {
#                'label': _('Express transactions'),
#                'url_name': 'paypal-express-list',
#            },
#        ]
#    })


OSCAR_SHOP_NAME = 'TEQUILA HM'
OSCAR_SHOP_TAGLINE = 'THM EN LINEA'
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)


AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Search Backend
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
    },
}


ROOT_URLCONF = 'maravatio.urls'

WSGI_APPLICATION = 'maravatio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.maravatio',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR
