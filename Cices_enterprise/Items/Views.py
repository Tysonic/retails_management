import os
from datetime import datetime
from flask_login import current_user
from flask_wtf import file
from Cices_enterprise import db, upload
from flask import render_template, redirect, flash, url_for
from Cices_enterprise.Computations import DataList
from Cices_enterprise.Computations.dropdowns import name_form_choice, packaging_form_choice, unit_form_choice, \
    brand_form_choice
from Cices_enterprise.Modules import ItemDetails
from Cices_enterprise.Modules.Items import Items
from Cices_enterprise.Items.Forms import AddItem
from flask import Blueprint, request
from werkzeug.utils import secure_filename
from Cices_enterprise.Uploads.Views import AddImage

items_blueprint = Blueprint("Items", __name__, template_folder="templates/items")


@items_blueprint.route("/items/list of items")
def list_of_items():
    names = ItemDetails.ItemNames.query.all()
    items_list = Items.query.all()

    return render_template("items.html", items=items_list, names=names, data_list=DataList)


@items_blueprint.route("/ details <_id>", methods=["GET", "POST"])
def details(_id):
    values = Items.query.filter_by(_Id=_id).first()
    return render_template("details.html", values=values)


@items_blueprint.route("/items/add new item", methods=["GET", "POST"])
def add_item():
    form = AddItem()
    brand_form_choice(form)
    unit_form_choice(form)
    name_form_choice(form)
    packaging_form_choice(form)

    if form.validate_on_submit() and request.method == 'POST':
        names = ItemDetails.ItemNames.query.filter_by(name_id=form.name.data).first()
        units = ItemDetails.ItemUnits.query.filter_by(unit_id=form.unit.data).first()
        # brands = ItemDetails.ItemBrands.query.filter_by(brand_id = form.brand.data)
        # packaging = ItemDetails.ItemPackaging.query.filter_by(packaging_id=form.packaging.data)
        item_value = names.name + " " + " " + str(form.size.data) + " " + units.unit
        new_items = Items(name=form.name.data, size=form.size.data, unit=form.unit.data, stock=form.initial.data,
                          packaging=form.packaging.data, brand=form.brand.data, created_by=current_user.username
                          , item=item_value)
        db.session.add(new_items)
        db.session.commit()
        return redirect(url_for("Items.list_of_items"))
    return render_template("add_items.html", form=form)


@items_blueprint.route("/items/update item details <_id>", methods=['GET', 'POST'])
def edit_item(_id):
    form = AddItem()
    values = Items.query.filter_by(_Id=_id).first()
    return render_template("edit_item.html", form=form, values=values)

@items_blueprint.route("/items/move item to trash <_id>")
def trash(_id):
    return render_template("trash.html")