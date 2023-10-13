from basic import app, db, Puppy

with app.app_context():

    my_puppy = Puppy('Rufus', 5)
    db.session.add(my_puppy)
    db.session.commit()

    ## READ
    all_puppies = Puppy.query.all()
    print(all_puppies)

    ## SELECT BY id
    puppy_one = db.session.get(Puppy, 1)
    print(puppy_one.name)

    ## FILTER BY name
    puppy_frankie = Puppy.query.filter_by(name='Frankie')
    print(puppy_frankie.all())

    ## UPDATE
    first_puppy = db.session.get(Puppy, 1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()

    ## DELETE
    second_puppy = db.session.get(Puppy, 2)
    db.session.delete(second_puppy)
    db.session.commit()

    all_puppies = Puppy.query.all()
    print(all_puppies)  