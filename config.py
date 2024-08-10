from os import path, environ
from dotenv import load_dotenv


BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, '.env'))


class Config:
    SECRET_KEY = environ.get('SECRET_KEY')

    # Flask Settings
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')

    # Database Settings
    MYSQL_HOST = environ.get('MYSQL_HOST')
    MYSQL_DATABASE = environ.get('MYSQL_DATABASE')
    MYSQL_USER = environ.get('MYSQL_USERNAME')
    MYSQL_PASSWORD = environ.get('MYSQL_PASSWORD')
