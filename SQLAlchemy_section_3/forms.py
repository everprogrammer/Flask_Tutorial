# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of puppy to remove:')
    submit = SubmitField('Remove Puppy')

    