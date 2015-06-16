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
    'paypal.standard',
    #'paypal.pro',
    'paypal.standard.ipn',
    'dashboard.cmproducts',
    'corsheaders',
    #'maravatioapp',
    'rest_framework',
    'rest_framework.authtoken'
] + get_core_apps(['checkout', 'shipping', 'catalogue', 'dashboard',
                   'dashboard.catalogue', 'dashboard.orders', 'basket',
                   'partner', 'customer', 'promotions'])

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
#CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITE_LIST = (
    'google.com',
    'http://192.168.1.3:9000/',
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

#paypal settings
PAYPAL_TEST = True
PAYPAL_DEBUG = True
#PAYPAL_WPP_USER = "eangel82_api1.gmail.com"
#PAYPAL_WPP_PASSWORD = "SSJNL5LK3DKS6FQJ"
#PAYPAL_WPP_SIGNATURE = "AFcWxV21C7fd0v3bYYYRCpSSRl31AEEsFlFVBPdnukiFEivDPqwaMeJr"
PAYPAL_RECEIVER_EMAIL = 'backend2.muchaweb@gmail.com'

#Oscar Settings
#PAYPAL_API_USERNAME = 'backend2.muchaweb-facilitator_api1.gmail.com'
#PAYPAL_API_PASSWORD = '4UPPDRXCPHJRRY5C'
#PAYPAL_API_SIGNATURE = 'AiPC9BjkCyDFQXbSkoZcgqH3hpacAhdkOcwnyfie6A21NvoIfMCOcR.L'

#PAYPAL_PAYFLOW_VENDOR_ID = 'RH3VFB4DGXFYW'

#PAYPAL_PAYFLOW_PASSWORD = 'Back2014'

#PAYPAL_PAYFLOW_CURRENCY = 'MXN'

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


OSCAR_DASHBOARD_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'icon-th-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Orders'),
        'icon': 'icon-shopping-cart',
        'url_name': 'dashboard:order-list',
        #'label': _('Fulfilment'),
        #'icon': 'icon-shopping-cart',
        #'children': [
        #    {
        #        'label': _('Orders'),
        #        'url_name': 'dashboard:order-list',
        #    },
            #{
            #    'label': _('Statistics'),
            #    'url_name': 'dashboard:order-stats',
            #},
            #{
            #    'label': _('Partners'),
            #    'url_name': 'dashboard:partner-list',
            #},
            # The shipping method dashboard is disabled by default as it might
            # be confusing. Weight-based shipping methods aren't hooked into
            # the shipping repository by default (as it would make
            # customising the repository slightly more difficult).
            #{
            #    'label': _('Shipping charges'),
            #    'url_name': 'dashboard:shipping-method-list',
            #},
        #]
    },
    {
        'label': _('Customers'),
        'icon': 'icon-group',
        'url_name': 'dashboard:users-index',
        #'children': [
        #    {
        #        'label': _('Customers'),
        #        'url_name': 'dashboard:users-index',
        #    },
        #    {
        #        'label': _('Stock alert requests'),
        #        'url_name': 'dashboard:user-alert-list',
        #    },
        #]
    },
    #{
    #    'label': _('Offers'),
    #    'icon': 'icon-bullhorn',
    #    'children': [
    #        {
    #            'label': _('Offers'),
    #            'url_name': 'dashboard:offer-list',
    #        },
    #        {
    #            'label': _('Vouchers'),
    #            'url_name': 'dashboard:voucher-list',
    #        },
    #    ],
    #},
    # {
    #     'label': _('Content'),
    #     'icon': 'icon-folder-close',
    #     'children': [
    #         {
    #             'label': _('Content blocks'),
    #             'url_name': 'dashboard:promotion-list',
    #         },
    #         {
    #             'label': _('Content blocks by page'),
    #             'url_name': 'dashboard:promotion-list-by-page',
    #         },
    #         {
    #             'label': _('Pages'),
    #             'url_name': 'dashboard:page-list',
    #         },
    #         {
    #             'label': _('Email templates'),
    #             'url_name': 'dashboard:comms-list',
    #         },
    #         {
    #             'label': _('Reviews'),
    #             'url_name': 'dashboard:reviews-list',
    #         },
    #     ]
    # },
    {
        'label': _('Reports'),
        'icon': 'icon-bar-chart',
        'url_name': 'dashboard:reports-index',
    },
    {
        'label': _('Catalogue'),
        'icon': 'icon-sitemap',
        'children': [
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': _('Product Types'),
                'url_name': 'dashboard:catalogue-class-list',
            },
            #{
            #    'label': _('Categories'),
            #    'url_name': 'dashboard:catalogue-category-list',
            #},
            #{
            #    'label': _('Ranges'),
            #    'url_name': 'dashboard:range-list',
            #},
            #{
            #    'label': _('Low stock alerts'),
            #    'url_name': 'dashboard:stock-alert-list',
            #},
        ]
    },
    {
        'label': _('Eventos'),
        'icon': 'icon-glass',
        'url_name': 'dashboard:event-list',
    },
    {
        'label': _('Plantillas'),
        'icon': 'icon-picture',
        'url_name': 'dashboard:template-list',
    },
]



THUMBNAIL_DEBUG = True


OSCAR_SHOP_NAME = ' '
OSCAR_SHOP_TAGLINE = ' '
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

LANGUAGE_CODE = 'es_MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "..", "static_local"),
#)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

#from oscar.defaults import *
try:
    from settings_local import *
except ImportError:
    pass