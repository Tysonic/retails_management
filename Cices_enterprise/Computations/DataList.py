from Cices_enterprise.Modules import  ItemDetails


def ItemNameList():
    return ItemDetails.ItemNames.query.all()


def ItemBrandList():
    return ItemDetails.ItemBrands.query.all()


def ItemUnitList():
    return ItemDetails.ItemUnits.query.all()


def ItemPackagingList():
    return ItemDetails.ItemPackaging.query.all()
