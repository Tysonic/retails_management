from Cices_enterprise.Purchases.Forms import AddPurchase
from flask import Blueprint
from Cices_enterprise import db
from Cices_enterprise.Modules.Items import Items
from Cices_enterprise.Modules.Purchases import Purchases
from flask import render_template, redirect, flash, url_for
from Cices_enterprise.Computations.Constants import item_form_choice
purchase_blueprint = Blueprint("Purchases",__name__, template_folder="templates/purchases")


@purchase_blueprint.route("/purchase/list of purchases", methods=["GET", "POST"])
def list_of_purchases():
    form = AddPurchase()
    purchases = Purchases.query.all()
    return render_template("purchases.html", purchases=purchases, form=form)

@purchase_blueprint.route("/purchases/add purchase record", methods = ["GET","POST"])
def add_purchase_record():
    form = AddPurchase()
    # item_list = []
    # select_list =[]
    # items = Items.query.all()
    # for item in items:
    #     item_list.append((item.Id,item.Name))
    item_form_choice(form)
    if form.validate_on_submit():
        new_purchase = Purchases(item_purchased=form.item.choices,price=form.price.data, date_purchased=None, quantity_purchased=form.quantity.data,
                                 purchased_by='', purchased_on=None, recorded_at=None )
        db.session.add(new_purchase)
        db.session.commit()
        return redirect(url_for("list_of_purchases"))
    return render_template("add_purchases.html", form=form)