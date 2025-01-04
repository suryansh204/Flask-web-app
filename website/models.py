#we want db model for our users and our notes
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#one to many relationship here

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    #relationship connecting two databases Note and USer(user.id connects to primary key of user database)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
   

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)# every object ahs a diff id
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    
    

