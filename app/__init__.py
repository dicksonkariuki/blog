from flask import Flask
from flask_bootstrap import Bootstrap 
from .Config import DevConfig
# initializing the application

app = Flask(__name__)

from app import views
#setting up the configuration
# initializing flask extensions
bootstrap = Bootstrap(app)