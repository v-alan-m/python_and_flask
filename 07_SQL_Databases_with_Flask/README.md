# Setup

- SQLite can scale well for basic applications that receieve around 100,000 daily hits
- To connect Python, Flask and SQL together an ORM (Object Relational Mapper) is implemented
    - The ORM will allow us to directly use Python instead of SQL syntax, to:
        - Create
        - Read
        - Update
        - Delete
    - The most common ORM for python is SQL Alchemy
        - Flask-SQLAlchemy is an extension that allows or easy connection with Flask
            - pip install Flask-SQLAlchemy


# Database (Reference: BasicModelApp.py)

- Set up SQLite database in a Flask app
- Create a model in the Flask app
- Perform basic CRUD on our model 

## Create a SQLite database
- Create a Flask app
- Configure the Flask app for SQLAlchemy
- Pass our application into the SQLAlchemy class

```Python
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
```


## Create a model

- The model will directly link to a table in a SQL database
- No need to manually create a table, using SQL
    - Table generated using a model class within python

- Create a model class
- Inherit from db.model 
- Optionally provide a table name
- Add in table coloumns as attributes
- Add in methods for __init__ and __repr__

## CRUD operations
- C: Create
- R: Read
- U: Update
- D: Delete


# Flask migrate

- When creating a model for a database table adjustments may need to take place
    - E.g Adding new columns
- After making these changes in the model, **migrate** these changes, so as to update the database table
<br></br>
- Can be done with Flask-Migrate
    - pip install Flask-Migrate

- Four main command lines
    - Set the FLASK_APP environment variable (when using a new or different model file is used): 
        - iOS: **export FLASK_APP=myapp.py**
        - Windows: **set FLASK_APP=myapp.py**
    - Set up the migrations directory
        - **flask db init**
    - Set up the migration file
        - **flask db migrate -m "some message"**
    - Update the database with the migration
        - **flask db upgrade**
    <br></br>
    - Change the model file, and update the file:
        - **flask db migrate -m "some message"**
        - **flask db upgrade**

## Flask Relationships

- For larger projects there are mulitple models
    - These models may have a relationship to each other
        - E.g A model for puppies, and a model for their owners
<br></br>
- Primary keys and foreign keys are used to understand model relationships
- **Primary key**: Unique identifier column
- **Foreign key**: Primary key in another table
<br></br>
### Intial structure
One .py file to:
- Create the structure of the data entries
- Create the data entries
- CRUD 

