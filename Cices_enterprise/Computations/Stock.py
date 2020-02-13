
#######################################################################################################################################
########## Current stock
########################
from Cices_enterprise.Computations.Query import query_all
from Cices_enterprise.Modules.Purchases import Purchases
from Cices_enterprise.Modules.Sales import Sales


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
