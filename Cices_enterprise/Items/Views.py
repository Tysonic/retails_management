from flask_login import current_user, login_required
from Cices_enterprise import db
from flask import render_template, redirect, url_for
from Cices_enterprise.Computations import Query
from Cices_enterprise.Computations.Stock import current_stock
from Cices_enterprise.Computations.dropdowns import name_form_choice, packaging_form_choice, unit_form_choice, \
    brand_form_choice
from Cices_enterprise.Modules import ItemDetails
from Cices_enterprise.Modules.ItemDetails import ItemNames, ItemUnits, ItemPackaging
from Cices_enterprise.Modules.Items import Items
from Cices_enterprise.Items.Forms import AddItem
from flask import Blueprint, request

from Cices_enterprise.Modules.Purchases import Purchases
from Cices_enterprise.Modules.Sales import Sales

items_blueprint = Blueprint("Items", __name__, template_folder="templates/items")


def item(_id):
    return Items.query.filter_by(_Id=_id)



###################################################################################################################################
########## Add items
#######################
@items_blueprint.route("/items/add new item", methods=["GET", "POST"])
@login_required
def add_item():
    form = AddItem()
    brand_form_choice(form)
    unit_form_choice(form)
    name_form_choice(form)
    packaging_form_choice(form)
    if form.validate_on_submit() and request.method == 'POST':
        names = ItemDetails.ItemNames.query.filter_by(_Id=form.name.data).first()
        units = ItemDetails.ItemUnits.query.filter_by(_Id=form.unit.data).first()
        item_value = names.name + " " + " " + str(form.size.data) + " " + units.unit
        new_items = Items(name=form.name.data, size=form.size.data, unit=form.unit.data,
                          packaging=form.packaging.data, brand=form.brand.data, created_by=current_user.username,
                          item=item_value)
        db.session.add(new_items)
        db.session.commit()
        return redirect(url_for("Items.list_of_items"))
    return render_template("add_items.html", form=form)

###################################################################################################################################
########## List of items
#######################
@items_blueprint.route("/items/list of items")
def list_of_items():
    stocks = current_stock()
    units = ItemUnits.query.all()
    names = ItemNames.query.all()
    packaging = ItemPackaging.query.all()
    items = Items.query.all()
    sales = Query.query_all(Sales)
    purchases = Query.query_all(Purchases)
    return render_template("items.html", items=items, names=names, units=units, packaging=packaging, sales=sales,
                           purchases=purchases, stocks=stocks)


@items_blueprint.route("/ details <_id>", methods=["GET", "POST"])
def item_details(_id):
    stocks=current_stock()
    return render_template("item_details.html", values=item(_id).first(),stocks=stocks)




###################################################################################################################################
########## Edit items
#######################
@items_blueprint.route("/items/update item details<_id>", methods=['GET', 'POST'])
def edit_item(_id):
    value = item(_id).first()
    form = AddItem(name=value.name, size=value.size, unit=value.unit, packging=value.packaging,
                   brand=value.brand)
    brand_form_choice(form)
    unit_form_choice(form)
    name_form_choice(form)
    packaging_form_choice(form)
    if form.validate_on_submit() and request.method == 'POST':
        names = ItemDetails.ItemNames.query.filter_by(name_id=form.name.data).first()
        units = ItemDetails.ItemUnits.query.filter_by(unit_id=form.unit.data).first()
        item_value = names.name + " " + " " + str(form.size.data) + " " + units.unit
        Items.query.filter_by(_Id=_id).update(
            dict(name=form.name.data, size=form.size.data, unit=form.unit.data,
                 packaging=form.packaging.data, brand=form.brand.data, item=item_value))
        db.session.commit()
        return redirect(url_for("Items.list_of_items"))
    return render_template("edit_items.html", form=form)


###################################################################################################################################
########## Delete items
#######################
@items_blueprint.route("/items/move item to trash<_id>")
def trash_item(_id):
    values = item(_id).first()
    return render_template("trash_items.html", values=values)


@items_blueprint.route("/delete item <_id>")
def delete(_id):
    values = item(_id).first()
    db.session.delete(values)
    db.session.commit()
    return redirect(url_for("Items.list_of_items"))
