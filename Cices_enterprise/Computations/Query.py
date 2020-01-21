from Cices_enterprise.Modules.Purchases import Purchases
from Cices_enterprise.Modules.Sales import Sales


def query_all(table):
    return table.query.all()


def query_one(table, _id):
    return table.query.filter_by(_Id=_id)



#######################################################################################################################################
########## Current stock
########################
def current_stock():
    val = {}
    purchases = query_all(Purchases)
    sales = query_all(Sales)
    for x in purchases:
        if x.item_purchased in val.keys():
            val[x.item_purchased] = val[x.item_purchased] + x.quantity_purchased
        else:
            val[x.item_purchased] = x.quantity_purchased
    for y in sales:
        val[y.item_sold] = val[y.item_sold] - y.quantity_sold
    return val
