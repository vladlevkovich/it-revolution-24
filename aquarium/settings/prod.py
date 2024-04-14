from aquarium.base import *
from dotenv import load_dotenv
import dj_database_url
import os

load_dotenv()

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
