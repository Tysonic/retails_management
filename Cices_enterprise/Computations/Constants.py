from Cices_enterprise.Modules.Items import Items
from Cices_enterprise.Modules.Purchases import Purchases


def item_form_choice(item_form):

    items = Items.query.all()
    item_names = []
    for item in items:
        item_names.append((item.Id,item.name))

    item_form.item.choices = item_names


