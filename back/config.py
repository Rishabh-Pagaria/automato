# Config for automato 
# WTF config
import sqlite3
class Config(object):

    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'the_very_secure_secret_security_key_that_no_will_ever_guess'

    # MySQL Config

    SQLALCHEMY_DATABASE_URI = 'sqlite:///automato.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RABBITMQ_HOST = "localhost"

    WEBDRIVER_PATH = r"C:\Users\padam\Downloads\chromedriver_win32\chromedriver.exe"
    TESTING = False

    UPLOAD_FOLDER = './../front/static/uploads'

