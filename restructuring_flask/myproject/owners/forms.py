# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Please enter name of the owner:')
    puppy_id = IntegerField('Please enter the id of the puppy:')
    submit = SubmitField('Add Owner')
    