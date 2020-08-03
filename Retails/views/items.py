from flask_login import current_user, login_required
from Retails.computations import Query
from datetime import datetime
from Retails.computations.Stock import current_stock

from Retails.modules.Items import Items
from Retails.forms.items import AddItem
from flask import request
from Retails import db
from flask import Blueprint, render_template, url_for, redirect

items_blueprint = Blueprint("items", __name__, template_folder="../templates/items")


###################################################################################################################################
########## Add items
#######################
@items_blueprint.route("/items/add new item", methods=["GET", "POST"])

def item_add():
    form = AddItem()
    if form.validate_on_submit() and request.method == 'POST':
        new_items = Items(name=form.name.data, size=form.size.data,unit_sales = form.unit_sales.data,
                          unit_stock = form.unit_stock.data,category = form.category.data,
                          sales_per_stock = form.sales_per_stock.data,created_at=datetime.utcnow(),
                          created_by=current_user.username, selling_price=form.selling_price.data,
                          buying_price=form.buying_price.data,archived=form.archived.data)
        db.session.add(new_items)
        db.session.commit()
        return redirect(url_for("items.item_add"))
    return render_template("item_add.html", form=form)





###################################################################################################################################
########## List of items
#######################
@items_blueprint.route("/items/list of items")
def item_list():
    items = Items.query.all()
    return render_template("item_list.html", items=items)


@items_blueprint.route("/ details <_id>", methods=["GET", "POST"])
def item_details(_id):
    stocks=current_stock()
    return render_template("item_details.html", values=Items.query.filter_by(id=_id).first(),stocks=stocks)




###################################################################################################################################
########## Edit items
#######################
@items_blueprint.route("/items/update item details<_id>", methods=['GET', 'POST'])
def item_update(_id):
    value = Items.query.filter_by(id=_id).first()

    form = AddItem(name=value.name, size=value.size, unit_sales=value.unit_sales, unit_stock=value.unit_stock,
                   sales_per_stock=value.sales_per_stock, category = value.category,buying_price=value.buying_price,
                   selling_price=value.selling_price,archived = value.archived)
    if form.validate_on_submit() and request.method == 'POST':

        Items.query.filter_by(id=_id).update(
            dict(name=form.name.data, size=form.size.data, unit_sales=form.unit_sales.data,
                 unit_stock=form.unit_stock.data, sales_per_stock=form.sales_per_stock.data,
                 selling_price=form.selling_price.data,buying_price=form.buying_price.data,
                 archived=form.archived.data,updated_by=current_user.username,updated_at=datetime.utcnow()))
        db.session.commit()
        return redirect(url_for("items.item_list"))
    return render_template("item_update.html", form=form)


###################################################################################################################################
########## Delete items
#######################
@items_blueprint.route("/items/move item to trash<_id>")
def item_trash(_id):
    values = Items.query.filter_by(_Id=_id).first()
    return render_template("item_trash.html", values=values)


@items_blueprint.route("/delete item <_id>")
def item_delete(_id):
    values = Items.query.filter_by(_Id=_id).first()
    db.session.delete(values)
    db.session.commit()
    return redirect(url_for("items.item_list"))

