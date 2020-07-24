from datetime import datetime
from flask_login import current_user
from werkzeug.utils import redirect
from Retails import db
from Retails.computations.dropdowns import initial_items_dropdown
from Retails.forms.initials import AddInitials
from Retails.modules.Items import Items
from Retails.modules.Initials import  InitialCash, InitialItems
from  flask import url_for, render_template
from flask import  Blueprint

initials_blueprint = Blueprint('initials', __name__, template_folder='../templates/initials')


@initials_blueprint.route("/add initial items", methods = ['GET','POST'])
def add_initials_items():
    form = AddInitials()
    initial_items_dropdown(form)
    if form.validate_on_submit():
        new = InitialItems(item= form.item_name.data, quantity = form.quantity.data, created_by = current_user.username, created_at = datetime.utcnow())
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('initials.list_initials'))
    return render_template('add_initial_items.html',form=form)


@initials_blueprint.route('/list initials', methods = ['POST', 'GET'])
def list_initials():
    initial_items = InitialItems.query.all()
    items = Items.query.all()

    cash = InitialCash.query.all()
    return render_template('list_initials.html', items=items, cash =cash, initial_items=initial_items)


@initials_blueprint.route("/add initial cash", methods = ['GET','POST'])
def add_initials_cash():
    form = AddInitials()

    if form.validate_on_submit():
        new = InitialCash(cash = form.item.data,  created_by = current_user.name, created_at = datetime.utcnow())
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('list_initials'))
    return render_template('add_initial_cash.html',form=form)


