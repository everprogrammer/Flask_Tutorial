from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprints = Blueprint('owners', __name__, template_folder='templates/owners')


@owners_blueprints.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        owner_name = form.name.data
        pup_id = form.puppy_id.data
        owner = Owner(owner_name, pup_id)
        db.session.add(owner)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    return render_template('owner.html', form=form)
