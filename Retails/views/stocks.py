from datetime import datetime

from flask_login import current_user

from Retails.computations.Query import query_one
from Retails.computations.dropdowns import item_purchased_dropdown
from Retails.forms.Stocks import AddPurchase
from flask import Blueprint
from Retails import db
from Retails.modules.Items import Items
from Retails.modules.Stocks import Stocks
from flask import render_template, redirect, flash, url_for

purchase_blueprint = Blueprint("stocks", __name__, template_folder="../templates/stocks")


@purchase_blueprint.route("/purchase/list of stocks", methods=["GET", "POST"])
def stock_list():
    form = AddPurchase()
    items = Items.query.all()
    stocks = Stocks.query.all()
    return render_template("stock_list.html", stocks=stocks, form=form, items=items)


@purchase_blueprint.route("/stocks/add purchase record", methods=["GET", "POST"])
def stock_add():
    form = AddPurchase()
    item_purchased_dropdown(form)
    if form.validate_on_submit():
        new_purchase = Stocks(item_purchased=form.item_purchased.data, unit_price=form.unit_price.data,
                                 quantity_purchased=form.quantity_purchased.data, updated_by="",
                                 purchased_by=current_user.username,supplier=form.supplier.data)
        db.session.add(new_purchase)
        db.session.commit()
        return redirect(url_for("stocks.stock_list"))
    return render_template("stock_add.html", form=form)


@purchase_blueprint.route('/stocks/ purchase  details <_id>')
def stock_details(_id):
    values=Stocks.query.filter_by(id=_id).first()
    items = Items.query.filter_by(id=values.item_purchased).first()
    return render_template('stock_details.html', values=values,items=items)


@purchase_blueprint.route('/stocks/edit purchase <_id> ', methods = ['GET', 'POST'])
def stock_update(_id):
    values = Stocks.query.filter_by(id = _id).first()
    form = AddPurchase(item_purchased=values.item_purchased, unit_price=values.unit_price, quantity_purchased=values.quantity_purchased,supplier=values.supplier)
    item_purchased_dropdown(form)
    if form.validate_on_submit():
        query_one(Stocks, _id).update(dict(item_purchased=form.item_purchased.data, unit_price=form.unit_price.data,
                                 quantity_purchased=form.quantity_purchased.data, updated_by= current_user.username
                                 ,supplier=form.supplier.data, updated_at=datetime.utcnow()))
        db.session.commit()
        return redirect(url_for("stocks.stock_list"))
    return render_template("stock_update.html",form=form, values=values)


@purchase_blueprint.route('/stocks/ purchase details <_id> ')
def stock_trash(_id):
    values = Stocks.query.filter_by(id = _id).first()
    return render_template("trash_stock.html", values=values)


@purchase_blueprint.route('/stocks/ delete purchase <_id>')
def stock_delete(_id):
    values = Stocks.query.filter_by(id = _id).first()
    db.session.delete(values)
    db.session.commit()
    return redirect(url_for('stocks.list'))