from flask import Flask
from .Config import DevConfig
# initializing the application

app = Flask(__name__)

from app import views