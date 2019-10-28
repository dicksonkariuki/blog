from flask import Flask
from flask_bootstrap import Bootstrap 
from .Config import DevConfig
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view ='auth.login'
# initializing the application
def create_app(config_name)



from app import views
#setting up the configuration
# initializing flask extensions
bootstrap = Bootstrap(app)