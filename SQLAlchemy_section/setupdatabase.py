from basic import app, db, Puppy


with app.app_context():
    # Create all the tables
    db.create_all()

    sam = Puppy('Sammy', 3)
    frank = Puppy('Frankie', 4)

    print(sam.id)
    print(frank.id)

    db.session.add_all([sam, frank])

    # commit changes to database
    db.session.commit()

    print(sam.id)
    print(frank.id)

