from flask_login import current_user

from Cices_enterprise.Computations.Query import query_one
from Cices_enterprise.Computations.dropdowns import item_purchased_dropdown
from Cices_enterprise.Purchases.Forms import AddPurchase
from flask import Blueprint
from Cices_enterprise import db
from Cices_enterprise.Modules.Items import Items
from Cices_enterprise.Modules.Purchases import Purchases
from flask import render_template, redirect, flash, url_for

purchase_blueprint = Blueprint("Purchases", __name__, template_folder="templates/purchases")


@purchase_blueprint.route("/purchase/list of purchases", methods=["GET", "POST"])
def list_of_purchases():
    form = AddPurchase()
    items = Items.query.all()
    purchases = Purchases.query.all()
    return render_template("purchases.html", purchases=purchases, form=form, items=items)


@purchase_blueprint.route("/purchases/add purchase record", methods=["GET", "POST"])
def add_purchase_record():
    form = AddPurchase()
    item_purchased_dropdown(form)
    if form.validate_on_submit():
        new_purchase = Purchases(item_purchased=form.item_purchased.data, unit_price=form.unit_price.data,
                                 quantity_purchased=form.quantity_purchased.data, updated_by="",
                                 purchased_by=current_user.username)
        db.session.add(new_purchase)
        db.session.commit()
        return redirect(url_for("Purchases.list_of_purchases"))
    return render_template("add_purchases.html", form=form)


@purchase_blueprint.route('/purchases/ purchase  details <_id>')
def purchase_details(_id):
    values=Purchases.query.filter_by(_Id=_id).first()
    return render_template('purchase_details.html', values=values)


@purchase_blueprint.route('/purchases/edit purchase <_id> ', methods = ['GET', 'POST'])
def edit_purchase(_id):
    values = Purchases.query.filter_by(_Id = _id).first()
    form = AddPurchase(item_purchased=values.item_purchased, unit_price=values.unit_price, quantity_purchased=values.quantity_purchased,)
    item_purchased_dropdown(form)
    if form.validate_on_submit():
        query_one(Purchases, _id).update(dict(item_purchased=form.item_purchased.data, unit_price=form.unit_price.data,
                                 quantity_purchased=form.quantity_purchased.data, updated_by= current_user.username
                                 ))
        db.session.commit()
        return redirect(url_for("Purchases.list_of_purchases"))
    return render_template("edit_purchases.html",form=form, values=values)


@purchase_blueprint.route('/purchases/ purchase details <_id> ')
def trash_purchase(_id):
    values = Purchases.query.filter_by(_Id = _id).first()
    return render_template("trash_purchases.html", values=values)


@purchase_blueprint.route('/purchases/ delete purchase <_id>')
def delete_purchase(_id):
    values = Purchases.query.filter_by(_Id = _id).first()
    db.session.delete(values)
    db.session.commit()
    return redirect(url_for('Purchases.list_of_purchases'))