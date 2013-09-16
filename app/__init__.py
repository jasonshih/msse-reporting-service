from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db, lm, bcrypt = MongoEngine(app), LoginManager(), Bcrypt(app)
lm.init_app(app)

from app import views, models
