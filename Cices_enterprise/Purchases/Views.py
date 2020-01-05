from flask_login import current_user
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


@purchase_blueprint.route('/purchases/ purchase <_id> details')
def details(_id):
    return
