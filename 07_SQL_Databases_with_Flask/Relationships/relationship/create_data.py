from models import db, Puppy, Owner, Toy

# Create 2 puppies
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# Add puppies to DB
db.session.add_all([rufus,fido])
db.session.commit()

# Check entries
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Create owner for Rufus, using the rufus object created above
jose = Owner('Jose', rufus.id)

# Give rufus some toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

# Check for those additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Show toys
rufus.report_toys()

# Delete things from the database:
# find_pup = Puppy.query.get(1)
# db.session.delete(find_pup)
# db.session.commit()