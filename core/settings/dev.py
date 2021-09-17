from decouple import config

from core.settings.base import BASE_DIR, os

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
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

###########################################
#          WSGI CONFIGURATION             #
###########################################
WSGI_APPLICATION = "core.wsgi.application"


###########################################
#           LOGGING CONFIGURATION         #
###########################################
try:
    from .log_settings import *
except Exception:
    pass
