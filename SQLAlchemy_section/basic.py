import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

baseDir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(baseDir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

# Create Model
class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old!"







