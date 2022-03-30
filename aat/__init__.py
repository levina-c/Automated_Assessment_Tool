from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
import os

app = Flask(__name__)

# define database
dbName = 'aat.db'
basedir = os.path.abspath(os.path.dirname(__file__))
finalpath = os.path.join(basedir, dbName)
destination = f"sqlite:///{finalpath}"

db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = '14a426c86b032eaa8f9eea231b7aa7c5ee72675114484cf54fea0c0ed2e16363eb402f2852855f1e5d830a7a5b06ee5b'

Bootstrap(app)
datepicker(app)

from aat import routes