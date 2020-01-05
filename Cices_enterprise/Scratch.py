from Cices_enterprise.Modules import ItemDetails
from Cices_enterprise.Modules.Items import  Items
from Cices_enterprise import db

names = ItemDetails.ItemNames.query.filter_by(name_id=2).first()
units = ItemDetails.ItemUnits.query.filter_by(unit_id=2).first()
item_value = names.name + " " + " " + str(600) + " " + units.unit
def select_item(_id=2):
    values = Items.query.filter_by(_Id=_id).update(dict(item = "Nichol"))
    db.session.commit()
    return values
select_item()
print(Items.query.filter_by(_Id=2).first())