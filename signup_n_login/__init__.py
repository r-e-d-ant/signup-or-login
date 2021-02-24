
from flask import Flask # first we import Flask
from flask_sqlalchemy import SQLAlchemy # import sqlalchemy orm
from flask_bcrypt import Bcrypt # import bcrypt for encrypting user passwords
from flask_login import LoginManager # flask login for user session management
#import pymysql

app = Flask(__name__)
# configuration
app.config['SECRET_KEY'] = "secret-key" # secret_key (required)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Users.db"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}/{3}".format("root", "2002mugisha", "127.0.0.1", "Users")

# Initializing
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# import routes module (otherwise get 404 not found)
from signup_n_login import routes