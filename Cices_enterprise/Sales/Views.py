from flask_login import current_user

from Cices_enterprise.Modules.Sales import Sales
from Cices_enterprise.Sales.Forms import AddSales
from flask import url_for, redirect, render_template, flash, Blueprint
from Cices_enterprise import db
from Cices_enterprise.Modules.Items import Items
def dropdown(item_selecte):
    items = Items.query.all()
    item_choise=[]
    for item in items:
        item_choise.append((item._Id, item.item))
    item_selecte.item_sold.choices=item_choise


sales_blueprint = Blueprint("Sales", __name__, template_folder="templates/sales")
@sales_blueprint.route("/sales/list of items sold", methods=["POST", "GET"])
def list_of_sales():
    form = AddSales()
    items = Items.query.all()
    sales = Sales.query.all()
    return render_template("sales.html", sales=sales, form=form, items = items)


@sales_blueprint.route("/sales/new sales record", methods = ['GET','POST'])
def add_new_sales():
    form = AddSales()
    dropdown(form)
    if form.validate_on_submit():
        new_sale = Sales(item_sold=form.item_sold.data, quantity_sold=form.quantity_sold.data,
                         unit_price=form.unit_price.data,
                          sold_by=current_user.username)
        db.session.add(new_sale)
        db.session.commit()
        return redirect(url_for("Sales.list_of_sales"))
    return render_template("add_sales.html", form=form)


