import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Setup the SQLite database
# Grab the current directory of this file
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Flask application
app = Flask(__name__)

# Connect Flask App to the Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Create model
# Inherit from db.Model class
class Puppy(db.Model):

    # Change the table name from the default, which will be the class name
    __tablename__ = 'puppies'

    # Create the columns: http://docs.sqlalchemy.org/en/latest/core/types.html
    
    # Create columns for the table, and defined data-types
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    
    # This sets what an instance in this table will have
    # The id will be auto-created later
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        # string representation, of a puppy in the model
        return f"Puppy {self.name} is {self.age} years old."
