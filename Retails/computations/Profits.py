from Retails.computations.Query import query_all
from Retails.modules.Purchases import Purchases
from Retails.modules.Sales import Sales


def profits():
    sales = query_all(Sales)
    purchases = Purchases.query.order_by(Purchases._Id.desc()).all()
    purchase_dict = {}
    sale_quantity_dict = {}
    sale_dict = {}
    profit = {}
    for purchase in purchases:
        if purchase.item_purchased in purchase_dict.keys():
            continue
        else:
            purchase_dict[purchase.item_purchased] = purchase.unit_price

    for sale in sales:
        if sale.item_sold in sale_quantity_dict.keys():
            sale_quantity_dict[sale.item_sold] += sale.quantity_sold
            sale_dict[sale.item_sold] += sale.quantity_sold * sale.unit_price
        else:
            sale_quantity_dict[sale.item_sold] = sale.quantity_sold
            sale_dict[sale.item_sold] = sale.quantity_sold * sale.unit_price

    for purchase in purchase_dict.keys():
        if purchase in sale_quantity_dict.keys():
            profit[purchase] = sale_dict[purchase] - purchase_dict[purchase] * sale_quantity_dict[purchase]

    return profit
