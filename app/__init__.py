from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
import os

app = Flask(__name__)

# configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI =\
    "sqlite:///"+os.path.join(basedir, 'data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
SECRET_KEY = "\x05e\xd6\xcd\xb23\xc8\x93Me"

MAIL_SERVER = "smtp.googlemail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

# create my first serious application :)
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)
mail = Mail(app)

from app import view
from app import models
