from Cices_enterprise.Modules import ItemDetails
from Cices_enterprise.Modules.Items import Items


def name_form_choice(item_form):
    items = ItemDetails.ItemNames.query.all()
    item_names = []
    for item in items:
        item_names.append((item._Id, item.name))
    item_form.name.choices = item_names


def unit_form_choice(item_form):
    items = ItemDetails.ItemUnits.query.all()
    item_names = []
    for item in items:
        item_names.append((item._Id, item.unit))
    item_form.unit.choices = item_names


def packaging_form_choice(item_form):
    items = ItemDetails.ItemPackaging.query.all()
    item_names = []
    for item in items:
        item_names.append((item._Id, item.packaging))
    item_form.packaging.choices = item_names


def brand_form_choice(item_form):
    items = ItemDetails.ItemBrands.query.all()
    item_names = []
    for item in items:
        item_names.append((item._Id, item.brand))
    item_form.brand.choices = item_names


def item_purchased_dropdown(item_form):
    items = Items.query.all()
    item_names = []
    for item in items:
        item_names.append((item._Id, item.item))
    item_form.item_purchased.choices = item_names


def sales_dropdown(item_selecte):
    items = Items.query.all()
    item_choise = []
    for item in items:
        item_choise.append((item._Id, item.item))
    item_selecte.item_sold.choices = item_choise
