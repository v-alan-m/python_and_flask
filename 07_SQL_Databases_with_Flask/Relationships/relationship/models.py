import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'date.sqlite' )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)


class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # ONE TO MANY: Connecting a single puppy to more than one toy
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')
    # ONE TO ONE: Connecting a single puppy to a single owner
    owner = db.relationship('Owner', backref='puppy', uselist=False)        # Only 1 value so no need to use a list, the default setting is to use a list

    # Create the ability to create new instances of puppy
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        # If the puppy has a stored owner
        if self.owner:
            return f"Puppy name is {self.name} and the owner's name is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet"

    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):
    
    __tablename__  = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Text, db.ForeignKey('puppies.id'))

    def __init__(self,item_name,puppy_id):
        self.item_name = item_name
        self.puppy_id =  puppy_id


class Owner(db.Model):
    
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    puppy_id = db.Column(db.Text, db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id