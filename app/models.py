from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin db.model):
    __tablename__ = 'users'
    """
    A user class that defines the user class and its objects
    """
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    post = db.relationship('post' bacref='user',lazy ='dynamic')
    user_id = db.relationship('comment',bacref='user',lazy ='dynamic')

    @property
    def password(self):
        raise AttributeError('This password is innacessible')

    @password.setter
    def password(self,password):
        self.password_hash= generate_password_hash(password)
    
    def verify_password(self,password):
    return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Post(db.model):
    """
    Post class that defines post tables in the database
    """
    __tablename__ = 'post'

    post_list = []

    id = db.Column(db.Integer,primary_key =True)
    actual_post = db.Column(db.String(255))
    vote_count = db.Column(db.String(255))
    category = db.Column(db.string(255))
    timestamp = db.Column(db.Datetime,index = True,default = datetime.utcnow)
    user_id = db.Column (db.Integer,db.ForeignKey('users_id'))
    post = db.relationship('Comment', backref = 'post',lazy = "dynamic")

    def save_post(self):
        """
        Function that saves the post created by blogers
        """
        db.session.add()
        db.session.commit()
class Comment(db.model):
    """
    Comment class that defines comment tables in the database
    """
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comments =db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users_id'))
    timestamp = db.Column(db.Datetime,index = True,default = datetime.utcnow)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'))


