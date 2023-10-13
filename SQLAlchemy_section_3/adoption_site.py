import os
from forms import AddForm, DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysec'

# SQL DATABASE SECTION
baseDir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

############################## Models
class Puppy(db.Model):

    __tablename__ = 'puppies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"


########## Views ####
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_puppy = Puppy(name)
        db.session.add(new_puppy)
        db.session.commit()

        return redirect(url_for('list_pup'))
    
    return render_template('add.html', form=form)

@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        pup = db.session.get(Puppy, id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)


