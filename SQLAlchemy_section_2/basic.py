# Create entries into the Tables

from models import app ,db, Puppy, Owner, Toy

with app.app_context():

    rufus = Puppy('Rufus')
    fido = Puppy('Fido')

    # Add puppies to database
    db.session.add_all([rufus, fido])
    db.session.commit()

    # Check all the puppies in the database
    print(Puppy.query.all())

    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)

    # Create owner object
    amir = Owner('Amir', rufus.id)

    # Give Rufus some toys
    toy1 = Toy('Chew Toy', rufus.id)
    toy2 = Toy('Ball', rufus.id)

    db.session.add_all([amir, toy1, toy2])
    db.session.commit()

    # Grab rufus after the additions
    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)

    print(rufus.report_num_toys())


