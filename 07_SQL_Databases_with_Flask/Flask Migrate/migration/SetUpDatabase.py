# Setup up the database

 
from BasicModelApp import db, Puppy     # Import db object and Puppy class


db.create_all()                         # Create the tables in the database

sam = Puppy('Sammy',3)                  # Create new entries in the database
frank = Puppy('Frankie',4)

print(sam.id)                           # Check ids (Not added to the database so should be None)
print(frank.id)

db.session.add_all([sam,frank])         # Ids will get created automatically once we add these entries to the DB

# db.session.add(sam)                   # Alternative for individual additions
# db.session.add(frank)

db.session.commit()                     # Now save it to the database

print(sam.id)                           # Check the ids
print(frank.id)
