"""
Django settings for seebeli project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'False')=='True'

if not DEBUG:
    ALLOWED_HOSTS = ['my.seebeli.ch','seebeli.juntagrico.science']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'seebeli',
    'juntagrico',
    'import_export',
    'fontawesomefree',
    'impersonate',
    'crispy_forms',
    'adminsortable2',
    'polymorphic',
]

ROOT_URLCONF = 'seebeli.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','seebeli.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'juntagrico.context_processors.vocabulary',
            ],
            'debug' : DEBUG
        },
    },
]

WSGI_APPLICATION = 'seebeli.wsgi.application'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

USE_TZ = True
TIME_ZONE = 'Europe/Zurich'

LANGUAGE_CODE = 'de'
DATE_INPUT_FORMATS =['%d.%m.%Y',]


AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
]

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

WHITELIST_EMAILS = []

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/"

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'


"""
     Import Export Settings
"""
IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'

"""
     juntagrico Settings
"""
VOCABULARY = {
    'member': 'Mitglied',
    'member_pl' : 'Mitglieder',
    'assignment' : 'Arbeitseinsatz',
    'assignment_pl' : 'Arbeitseinsätze',
    'share' : 'Mitgliedsbeitrag',
    'share_pl' : 'Mitgliedsbeiträge',
    'subscription' : 'Abo',
    'subscription_pl' : 'Abos',
    'co_member' : 'Mitabonnent',
    'co_member_pl' : 'Mitabonnenten',
    'price' : 'Betriebsbeitrag',
    'member_type' : 'Mitglied',
    'member_type_pl' : 'Mitglieder',
    'depot' : 'Depot',
    'depot_pl' : 'Depots',
    'package': 'Tasche',
}

ORGANISATION_NAME = "Solawi Seebeli"
ORGANISATION_LONG_NAME = "Solawi Seebeli"
ORGANISATION_ADDRESS = {"name":"Solawi Seebeli", 
            "street" : "Seebeli",
            "number" : "67",
            "zip" : "9405",
            "city" : "Wienacht",
            "extra" : ""}
ORGANISATION_BANK_CONNECTION = {"PC" : "123",
            "IBAN" : "CH24 0839 0038 2424 1000 0",
            "BIC" : "ABSOCH22",
            "NAME" : "Alternative Bank Schweiz",
            "ESR" : "01-9252-0"}
ORGANISATION_WEBSITE = {
    'name': "www.seebeli.ch",
    'url': "https://www.seebeli.ch"
}

ENABLE_SHARES = False
ENABLE_SHARES = "False"  # TODO: fixme
SHARE_PRICE = "100"

CONTACTS = {
    "general": "info@seebeli.ch"
}
CURRENCY = "CHF"
BUSINESS_YEAR_START = {"day": 1, "month": 2}
MEMBERSHIP_END_MONTH = 12
BUSINESS_YEAR_CANCELATION_MONTH = 9
ENABLE_REGISTRATION = True
BYLAWS = "https://uploads.strikinglycdn.com/files/e143b0c4-7513-49a6-928c-3d466e52fabe/Statuten%20Solawi%20Seebeli%202021-04-12.pdf?id=3403441"
STYLES = {'static': ['seebeli/css/customize.css']}

# Staging
if os.environ.get('JUNTAGRICO_STAGING') == '1':
    # staging URL erlauben
    ALLOWED_HOSTS.append('seebeli-staging.juntagrico.science')
    # E-Mails Deaktivieren
    EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
