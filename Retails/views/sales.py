from datetime import date, datetime

from flask_login import current_user
from wtforms import ValidationError
from Retails.computations.Query import query_one
from Retails.computations.Stock import current_stock
from Retails.computations.dropdowns import sales_dropdown
from Retails.modules.Sales import Sales
from Retails.forms.sales import AddSales
from flask import url_for, redirect, render_template, flash, Blueprint
from Retails import db
from Retails.modules.Items import Items


def sale(_id):
    return Sales.query.filter_by(id=_id)


sales_blueprint = Blueprint("sales", __name__, template_folder="../templates/sales/")


@sales_blueprint.route("/sales/list of items sold", methods=["POST", "GET"])
def sale_list():
    form = AddSales()
    items = Items.query.all()
    sales = Sales.query.all()
    return render_template("sale_list.html", sales=sales, form=form, items=items)


@sales_blueprint.route("/sales/new sales record", methods=['GET', 'POST'])
def sale_add():
    form = AddSales()
    sales_dropdown(form)

    if form.validate_on_submit():
        new_sale = Sales(item=form.item.data, quantity=form.quantity.data,
                             price=form.price.data,
                             sold_by=current_user.username, sold_at = date.today())
        db.session.add(new_sale)
        db.session.commit()
        return redirect(url_for("sales.sale_list"))
    return render_template("sale_add.html", form=form)



@sales_blueprint.route('/sales/ edit sales <_id>', methods=['GET', 'POST'])
def sale_update(_id):
    values = sale(_id).first()
    form = AddSales(item=values.item_sold, quantity=values.quantity_sold,
                    price=values.unit_price)
    sales_dropdown(form)
    if form.validate_on_submit():
        sale(_id).update(dict(item_sold=form.item_sold.data, quantity_sold=form.quantity_sold.data,
                              unit_price=form.unit_price.data,updated_by=current_user.username,updated_at=datetime.utcnow()))
        db.session.commit()
        message = "Values updated successfully to!"
        return redirect(url_for("sales.details", _id=values._Id, message=message))
    return render_template("sale_update.html", form=form)


@sales_blueprint.route('/sales/ sales details <_id>')
def sale_details(_id):
    values = sale(_id).first()
    return render_template("sale_details.html", sale=sale(_id), values=values)


@sales_blueprint.route('/sales/ trash sales <_id>')
def sale_trash(_id):
    values = sale(_id).first()
    return render_template("sale_trash.html", sale=sale(_id), values=values)


@sales_blueprint.route('/sales delete sales <_id>')
def sale_delete(_id):
    sales = sale(_id).first()
    db.session.delete(sales)
    db.session.commit()
    return redirect(url_for("sales.list"))
