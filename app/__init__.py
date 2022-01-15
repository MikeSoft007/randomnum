
from flask import Flask
from config import Config
from flask_pymongo import PyMongo
from flask_restful import Api
from flask_cors import CORS


# creating the flask app
app = Flask(__name__)
app.config.from_object(Config)

# creating an API object
api = Api(app)

CORS(app)

mongo = PyMongo(app)

from app import routes