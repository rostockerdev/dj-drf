from decouple import config

from core.settings.base import BASE_DIR

from .base import *

###########################################
#        SECRET CONFIGURATION             #
###########################################

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


###########################################
#        DATABASE CONFIGURATION           #
###########################################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default=5432, cast=int),
    }
}

###########################################
#          WSGI CONFIGURATION             #
###########################################
WSGI_APPLICATION = "core.wsgi.application"

###########################################
#        SECURITY CONFIGURATION           #
###########################################
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False

###########################################
#           EMAIL CONFIGURATION           #
###########################################
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT", default=25, cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=False, cast=bool)

###########################################
#           LOGGING CONFIGURATION         #
###########################################
try:
    from .log_settings import *
except Exception:
    pass

try:
    from .language_settings import *
except Exception:
    pass
