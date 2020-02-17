# The table has been created by running BasicModelApp and SetUpDatabase we can play around with CRUD commands
# Our goal here is to just familiarize ourselves with CRUD commands

from BasicModelApp import db,Puppy


# Create
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()


# Read
# ORM filter options: Filter(), filter_by(), limit(), order_by(), group_by()
# Executor options: all(), first(), get(), count(), paginate()

# list of all puppies in table
all_puppies = Puppy.query.all() 
print(all_puppies)
print('\n')

# Grab by id
puppy_one = Puppy.query.get(1)
print(puppy_one)
print(puppy_one.age)
print('\n')

# Filters
puppy_sam = Puppy.query.filter_by(name='Sammy') # Returns list
print(puppy_sam)
print('\n')


# Update
# Grab data, modify, then save changes.
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


# Delete
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()


# Check for changes:
all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies)
