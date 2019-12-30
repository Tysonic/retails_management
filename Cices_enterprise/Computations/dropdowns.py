from Cices_enterprise.Modules import ItemDetails


def name_form_choice(item_form):
    items = ItemDetails.ItemNames.query.all()
    item_names = []
    for item in items:
        item_names.append((item.name_id, item.name))
    item_form.name.choices = item_names


def unit_form_choice(item_form):
    items = ItemDetails.ItemUnits.query.all()
    item_names = []
    for item in items:
        item_names.append((item.unit_id, item.unit))
    item_form.unit.choices = item_names


def packaging_form_choice(item_form):
    items = ItemDetails.ItemPackaging.query.all()
    item_names = []
    for item in items:
        item_names.append((item.packaging_id, item.packaging))
    item_form.packaging.choices = item_names


def brand_form_choice(item_form):
    items = ItemDetails.ItemBrands.query.all()
    item_names = []
    for item in items:
        item_names.append((item.brand_id, item.brand))
    item_form.brand.choices = item_names
