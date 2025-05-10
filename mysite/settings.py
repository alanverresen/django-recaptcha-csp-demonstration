import json

from pathlib import Path

from csp.constants import SELF
from django.utils.crypto import get_random_string


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_string(32)

# SECURITY WARNING: never add this file to version control
with open(BASE_DIR / "secrets.json", "r") as f:
    SECRETS = json.load(f)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "myapp",
    "django_recaptcha",
    "csp",
]

MIDDLEWARE = [
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
    },
]

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

# django-recaptcha
SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']

# django-csp
CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        "default-src": [SELF],
    },
}
