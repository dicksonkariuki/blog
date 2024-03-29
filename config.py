import os

class Config:
    '''
    This is the general configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:karis300@localhost/bloger'

    SECRET_KEY = os.environ.get('SECRET_KEY')


    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    This is the production configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class DevConfig(Config):
    DEBUG =True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}
