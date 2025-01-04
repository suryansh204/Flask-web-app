#we want db model for our users and our notes
from . import db 
from flask_login import UserMixin

class Note(db.Model):
    id = db.Coloumn(db.Integer, primary_key=True)
    data = db.Coloumn(db.String(10000))
    date = db.Coloumn(db.DateTime(timezone=True), default=func.now())
    

class User(db.Model, UserMixin):
    id = db.coloumn(db.Integer, primary_key=True)# every object ahs a diff id
    email = db.Coloumn(db.String(150), unique=True)
    password = db.coloumn(db.String(150))
    firstName = db.coloumn(db.String(150))
    
    

