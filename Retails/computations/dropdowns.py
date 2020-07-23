from Retails.modules.Items import Items

def item_purchased_dropdown(item_form):
    items = Items.query.all()
    item_names = []
    for item in items:
        item_names.append((item.id, item.name+" " +item.size))
    item_form.item_purchased.choices = item_names


def sales_dropdown(item_selecte):
    items = Items.query.all()
    item_choise = []
    for item in items:
        item_choise.append((item.id, item.name+" "+item.size))
    item_selecte.item_sold.choices = item_choise


def sales_dropdown(item_selecte):
    items = Items.query.all()
    item_choise = []
    for item in items:
        item_choise.append((item.id, item.name+" "+item.size))
    item_selecte.item.choices = item_choise


def initial_items_dropdown(item_selecte):
    items = Items.query.all()
    item_choise = []
    for item in items:
        item_choise.append((item.id, item.name+" "+item.size))
    item_selecte.item_name.choices = item_choise
