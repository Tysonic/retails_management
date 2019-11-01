from Cices_enterprise.Purchases.Forms import AddPurchase
from flask import Blueprint
from Cices_enterprise import db
from Cices_enterprise.Modules.Items import Items
from Cices_enterprise.Modules.Purchases import Purchases
from flask import render_template, redirect, flash, url_for
purchase_blueprint = Blueprint("Purchases",__name__, template_folder="templates/purchases")

def item_form_choice(item_form):
    items = Items.query.all()
    item_names = []
    for item in items:
        item_names.append((item.Id,item.name))
    item_form.item_purchased.choices = item_names


@purchase_blueprint.route("/purchase/list of purchases", methods=["GET", "POST"])
def list_of_purchases():
    form = AddPurchase()
    purchases = Purchases.query.all()
    return render_template("purchases.html", purchases=purchases, form=form)

@purchase_blueprint.route("/purchases/add purchase record", methods = ["GET","POST"])
def add_purchase_record():
    form = AddPurchase()
    item_form_choice(form)
    if form.validate_on_submit():
        new_purchase = Purchases(item_purchased=form.item_purchased.data,unit_price=2000, quantity_purchased=form.quantity_purchased.data, updated_by="", purchased_by="Nicholas")
        db.session.add(new_purchase)
        db.session.commit()
        return redirect(url_for("Purchases.list_of_purchases"))
    return render_template("add_purchases.html", form=form)
