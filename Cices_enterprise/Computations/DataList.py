from Cices_enterprise.Modules import ItemDetails
from Cices_enterprise.Modules.Items import Items
from Cices_enterprise.Modules.Purchases import Purchases


def item_names():
    return ItemDetails.ItemNames.query.all()


def item_brands():
    return ItemDetails.ItemBrands.query.all()


def item_units():
    return ItemDetails.ItemUnits.query.all()


def item_packaging():
    return ItemDetails.ItemPackaging.query.all()


def items():
    return Items.query.all()


def item(_id):
    return Items.query.filter_by(_Id=_id).first()


def purchase(_id):
    return Purchases.query.filter_by(purchase_id=_id)
