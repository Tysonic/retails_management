from Cices_enterprise.Purchases.Forms import AddPurchase
from flask import Blueprint
from Cices_enterprise import db
from Cices_enterprise.Modules.Purchases import Purchases
from flask import render_template, redirect, flash, url_for
purchase_blueprint = Blueprint("Purchases",__name__, template_folder="templates/purchases")


@purchase_blueprint.route("/purchase/list of purchases")
def list_of_purchases():
    form = AddPurchase()
    purchases = Purchases.query.all()
    return render_template("purchases.html", purchases=purchases, form=form)

@purchase_blueprint.route("/purchases/add purchase record")
def add_purchase_record():
    form = AddPurchase()
    if form.validate_on_submit():
        new_purchase = Purchases(price=form.price.data, date_purchased=None, quantity_purchased=form.quantity.data,
                                 purchased_by='', purchased_on=None, recorded_at=None, item_purchased="")
        db.session.add(new_purchase)
        db.session.commit()
        return redirect(url_for("list_of_purchases"))
    return render_template("add_purchases.html", form=form)