# Puppy adoption site

python 3.7  
*(Create virtual environment of python 3.7 if time module error is presented when running more recent versions of python (i.e python 3.8))*

**Only run the python file, to run the Flask app. However if the "migrations" folder and "data.sqliye" file is deleted or modified then then use the instructions below**s

## Set up database (migration) - SQLite

### iOS
    export FLASK_APP=adoption_site.py
### Windows
    set FLASK_APP=adoption_site.py

### Create the migrations folder
    flask db init

### Set up the migration file
    flask db migrate -m "some message"

### Update the database with the migration
    flask db upgrade

### Run the python file
    python adoption_site.py