
#######################################################################################################################################
########## Current stock
########################
from Retails.computations.Query import query_all
from Retails.modules.Stocks import Stocks
from Retails.modules.Sales import Sales


def current_stock():
    val = {}
    purchases = query_all(Stocks)
    sales = query_all(Sales)
    for x in purchases:
        if x.item_purchased in val.keys():
            val[x.item_purchased] = val[x.item_purchased] + x.quantity_purchased
        else:
            val[x.item_purchased] = x.quantity_purchased
    for y in sales:
        val[y.item] = val[y.item] - y.quantity
    return val
