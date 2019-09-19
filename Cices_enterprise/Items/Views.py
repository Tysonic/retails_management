from Cices_enterprise import db
from flask import render_template, redirect, flash, url_for
from Cices_enterprise.Modules.Items import Items
from Cices_enterprise.Items.Forms import AddItem
from flask import Blueprint


items_blueprint = Blueprint("Items", __name__, template_folder="templates/items")


@items_blueprint.route("/items/list of items")
def list_of_items():
    items_list = Items.query.all()
    return render_template("items.html",items=items_list)


@items_blueprint.route("/items/add new item", methods = ["GET","POST"])
def add_item():
    form = AddItem()
    if form.validate_on_submit():
        new_items = Items(name=form.item.data, size=form.size.data, unit=form.unit.data,
                          packaging=form.packaging.data, created_by="", created_at=None)
        db.session.add(new_items)
        db.session.commit()
        return redirect(url_for("Items.list_of_items"))
    return render_template("add_items.html", form = form)


@items_blueprint.route("/items/update item details", methods = ['GET','POST'])
def update_item_details(id):
    #form =
    #edit_item = Items.query.filter_by(Id==)
    return "update item properties"
