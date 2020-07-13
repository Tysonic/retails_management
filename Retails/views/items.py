from flask_login import current_user, login_required
from Retails import db
from flask import render_template, redirect, url_for
from Retails.computations import Query
from Retails.computations.Stock import current_stock
from Retails.computations.dropdowns import name_form_choice, packaging_form_choice, unit_form_choice, \
    brand_form_choice
from Retails.modules import ItemDetails
from Retails.modules.ItemDetails import ItemNames, ItemUnits, ItemPackaging
from Retails.modules.Items import Items
from Retails.forms.items import AddItem
from flask import Blueprint, request
from wtforms import ValidationError
from Retails import db
from flask import Blueprint, render_template, url_for, redirect
from Retails.computations.Query import query_one, query_all
from Retails.modules import ItemDetails
from Retails.modules.Purchases import Purchases
from Retails.modules.Sales import Sales

items_blueprint = Blueprint("items", __name__, template_folder="staffs/items")


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
        return redirect(url_for("items.list_of_items"))
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
        return redirect(url_for("items.list_of_items"))
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
    return redirect(url_for("items.list_of_items"))

items_details_blueprint = Blueprint("Advanced", __name__, template_folder="staffs/itemDetails")


@items_details_blueprint.route("/add new item type", methods=["GET", "POST"])
def advanced():
    form = Advanced()
    if form.validate_on_submit():
        try:
            if form.packaging.data == form.item.data == form.brand.data == form.unit.data == "":
                raise ValidationError(message="Please select a field to submit")
            else:
                if form.item.data is not "":
                    new = ItemDetails.ItemNames(name=form.item.data)
                    db.session.add(new)
                if form.unit.data is not "":
                    new = ItemDetails.ItemUnits(unit=form.unit.data)
                    db.session.add(new)
                if form.brand.data is not "":
                    new = ItemDetails.ItemBrands(brand=form.brand.data)
                    db.session.add(new)
                if form.packaging.data is not "":
                    new = ItemDetails.ItemPackaging(packaging=form.packaging.data)
                    db.session.add(new)
        except Exception as e:
            return render_template("advanced.html", form=form, error=e)

        db.session.commit()
        return redirect(url_for("Advanced.advance_list"))

    return render_template("advanced.html", form=form)


@items_details_blueprint.route("/list of item types")
def advance_list():
    names = query_all(ItemDetails.ItemNames)
    units = query_all(ItemDetails.ItemUnits)
    packaging = query_all(ItemDetails.ItemPackaging)
    brands = query_all(ItemDetails.ItemBrands)
    return render_template("advance_list.html", names=names,units=units, brands = brands, packaging = packaging)
