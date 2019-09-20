from Cices_enterprise.Modules.Sales import Sales
from Cices_enterprise.Sales.Forms import AddSales
from flask import url_for, redirect, render_template, flash, Blueprint
from Cices_enterprise import db


sales_blueprint = Blueprint("Sales", __name__, template_folder="templates/sales")
@sales_blueprint.route("/sales/list of items sold", methods=["POST", "GET"])
def list_of_sales():
    form = AddSales()
    sales = Sales.query.all()
    return render_template("sales.html", sales=sales, form=form)


@sales_blueprint.route("/sales/new sales record")
def add_new_sales():
    form = AddSales()
    if form.validate_on_submit():
        new_sale = Sales(item_sold="", quantity_sold=form.quantity.data, date_sold=form.sold_on.data,
                         price=form.price.data,
                         unit_sold=form.unit.data, recorded_at=None, sold_by="")
        db.session.add(new_sale)
        db.session.commit()
        return redirect(url_for("list_of_items"))
    return render_template("add_sales.html")


