from wtforms import ValidationError

from Cices_enterprise import db
from flask import Blueprint, render_template, url_for, redirect
from Cices_enterprise.Modules import ItemDetails
from Cices_enterprise.Items.ItemDetails.ItemDetailsForm import Advanced

items_details_blueprint = Blueprint("Advanced", __name__, template_folder="templates/itemDetails")


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
        return redirect(url_for("Advanced.brand_list"))

    return render_template("advanced.html", form=form)


@items_details_blueprint.route("/list of item types")
def name_list():
    names = ItemDetails.ItemNames.query.all()
    return render_template("names_list.html", names=names)


@items_details_blueprint.route("/list of item destributors")
def brand_list():
    return render_template("brand_list.html")


@items_details_blueprint.route("/list of items packaging")
def packaging_list():
    return render_template("name_list.html")


@items_details_blueprint.route("/list of item units")
def unit_list():
    return render_template("name_list.html")
