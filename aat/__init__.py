from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_required


app = Flask(__name__)
Bootstrap(app)

app.config["SECRET_KEY"]='3dcbb92fcf85643723af1816350b07d4811c3f8e4cade554'

# SQLite database 

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir,'my_db.db')}"


# db = SQLAlchemy(app)


from blog import routes
