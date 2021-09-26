from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret_key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:pwroot@localhost/recipe_db'

db = SQLAlchemy(app)
Migrate(app,db)

from recipe_api.models import RecipeModel

api = Api(app)

from recipe_api import apis