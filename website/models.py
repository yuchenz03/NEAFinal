from . import db #Import all from db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Squads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    squadName = db.Column(db.String(150), unique=True)
    squadCode = db.Column(db.String(4), unique=True)
    
    
class User(db.Model, UserMixin): #Creating the user model
    id = db.Column(db.Integer, primary_key=True) #This userID is the primary key and unique to each user
    forename = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True) #unique=True ensures that no users have duplicate emails and usernames
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) #The date and time when this is stored is saved as a new column
    role = db.Column(db.String(7))
    