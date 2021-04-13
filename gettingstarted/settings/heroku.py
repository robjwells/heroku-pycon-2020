"""
Production settings for Heroku.
"""

import environ

from gettingstarted.settings.base import *


env = environ.Env(
    # Set casting, default value
    DEBUG=(bool, False),
)

# False if unset in the environment.
DEBUG = env("DEBUG")

# Raises ImproperlyConfigured if unset in environment.
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    # Raises ImproperlyConfigured if "DATABASE_URL" unset in environment.
    "default": env.db()
}
