from aquarium.settings import *
from dotenv import load_dotenv
import dj_database_url
import os

load_dotenv()

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': dj_database_url.parse(os.getenv('DB_URL'), conn_max_age=600)
}
