from flask_login import UserMixin
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
    def
