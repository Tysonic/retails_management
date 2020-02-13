from flask_login import current_user
from wtforms import ValidationError
from Cices_enterprise.Computations.Query import query_one
from Cices_enterprise.Computations.Stock import current_stock
from Cices_enterprise.Computations.dropdowns import sales_dropdown
from Cices_enterprise.Modules.Sales import Sales
from Cices_enterprise.Sales.Forms import AddSales
from flask import url_for, redirect, render_template, flash, Blueprint
from Cices_enterprise import db
from Cices_enterprise.Modules.Items import Items


def sale(_id):
    return Sales.query.filter_by(_Id=_id)


sales_blueprint = Blueprint("Sales", __name__, template_folder="templates/sales")


@sales_blueprint.route("/sales/list of items sold", methods=["POST", "GET"])
def list_of_sales():
    form = AddSales()
    items = Items.query.all()
    sales = Sales.query.all()
    return render_template("sales.html", sales=sales, form=form, items=items)


@sales_blueprint.route("/sales/new sales record", methods=['GET', 'POST'])
def add_new_sales():
    form = AddSales()
    sales_dropdown(form)
    stocks = current_stock()
    try:
        if form.validate_on_submit():
            if form.item_sold.data in stocks.keys():
                if (stocks[form.item_sold.data]-form.quantity_sold.data)<0:
                    raise ValidationError(message="You only have {} items left in stock\n please make a valid selection of {} or less items".format(stocks[form.item_sold.data],stocks[form.item_sold.data]))
                else:
                    new_sale = Sales(item_sold=form.item_sold.data, quantity_sold=form.quantity_sold.data,
                                     unit_price=form.unit_price.data,
                                     sold_by=current_user.username)
                    db.session.add(new_sale)


            else:
                val = query_one(Items,form.item_sold.data).first()
                raise ValidationError("You haven't created a stocked\n for"+ val.item+"Please go to\n purchases>>new purchases and create stock for this item".format(form.quantity_sold.data))
            db.session.commit()
            return redirect(url_for("Sales.list_of_sales"))
        return render_template("add_sales.html", form=form)
    except Exception as e:
        # form = AddSales(item_sold=form.item_sold.data, quantity_sold=form.quantity_sold.data,
        #                              unit_price=form.unit_price.data)
        return render_template("add_sales.html", form=form, error=e)
        


@sales_blueprint.route('/sales/ edit sales <_id>', methods=['GET', 'POST'])
def edit_sales(_id):
    values = sale(_id).first()
    form = AddSales(item_sold=values.item_sold, quantity_sold=values.quantity_sold,
                    unit_price=values.unit_price)
    sales_dropdown(form)
    if form.validate_on_submit():
        sale(_id).update(dict(item_sold=form.item_sold.data, quantity_sold=form.quantity_sold.data,
                              unit_price=form.unit_price.data))
        db.session.commit()
        message = "Values updated successfully to!"
        return redirect(url_for("Sales.sales_details", _id=values._Id, message=message))
    return render_template("edit_sales.html", form=form)


@sales_blueprint.route('/sales/ sales details <_id>')
def sales_details(_id):
    values = sale(_id).first()
    return render_template("sales_details.html", sale=sale(_id), values=values)


@sales_blueprint.route('/sales/ trash sales <_id>')
def trash_sales(_id):
    values = sale(_id).first()
    return render_template("trash_sales.html", sale=sale(_id), values=values)


@sales_blueprint.route('/sales delete sales <_id>')
def delete_sales(_id):
    sales = sale(_id).first()
    db.session.delete(sales)
    db.session.commit()
    return redirect(url_for("Sales.list_of_sales"))
