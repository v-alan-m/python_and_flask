import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate                                                               # Include the Flask-Migrate library



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)                                                                                # Middle man to connect the the application (app) to the database (db), to add migration capabilities


class Puppy(db.Model):

    __tablename__ = 'puppies'


    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)  
    

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age

    def __repr__(self):
        # string representation, of a puppy in the model
        return f"Puppy {self.name} is {self.age} years old."
