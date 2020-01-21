from wtforms import ValidationError

from Cices_enterprise import db
from flask import Blueprint, render_template, url_for, redirect

from Cices_enterprise.Computations.Query import query_one, query_all
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
        return redirect(url_for("Advanced.advance_list"))

    return render_template("advanced.html", form=form)


@items_details_blueprint.route("/list of item types")
def advance_list():
    names = query_all(ItemDetails.ItemNames)
    units = query_all(ItemDetails.ItemUnits)
    packaging = query_all(ItemDetails.ItemPackaging)
    brands = query_all(ItemDetails.ItemBrands)
    return render_template("advance_list.html", names=names,units=units, brands = brands, packaging = packaging)





