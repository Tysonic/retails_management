from Cices_enterprise import db
from flask import Blueprint, render_template

from Cices_enterprise.Computations.Query import query_all, query_one
from Cices_enterprise.Modules.Items import Items
from Cices_enterprise.Modules.Purchases import Purchases
from Cices_enterprise.Modules.Sales import Sales
from Cices_enterprise.Sales.Forms import AddSales

dashboard_blueprint = Blueprint('Dashboard',__name__,template_folder='templates/dashboard')


@dashboard_blueprint.route('/Cice shoppers Dashboard', methods=['GET', 'POST'])
def dashboard():
    items = query_all(Items)
    sales = query_all(Sales)
    purchases = query_all(Purchases)
    total_sales = 0
    total_purchases = 0
    for sale in sales:
        total_sales+=(sale.unit_price*sale.quantity_sold)

    for purchase in purchases:
        total_purchases +=(purchase.unit_price*purchase.quantity_purchased)

    return render_template("dashboard.html",total_purchases=total_purchases,total_sales=total_sales)


@dashboard_blueprint.route('/sales summery ')
def sales_summery():
    sales = query_all(Sales)
    items = query_all(Items)
    price = {}
    quantity = {}
    unit_price ={}
    for sale in sales:
        if sale.item_sold in price.keys():
            price[sale.item_sold] += sale.quantity_sold*sale.unit_price
        else:
            price[sale.item_sold] = sale.quantity_sold*sale.unit_price


    for sale in sales:
        if sale.item_sold in unit_price.keys():
            unit_price[sale.item_sold] += sale.quantity_sold*sale.unit_price
        else:
            unit_price[sale.item_sold] = sale.quantity_sold*sale.unit_price

    for sale in sales:
        if sale.item_sold in quantity.keys():
            quantity[sale.item_sold] += sale.quantity_sold
        else:
            quantity[sale.item_sold] = sale.quantity_sold
            
    return render_template("sales_summery.html", price=price, quantity=quantity, items = items,sales=sales)


@dashboard_blueprint.route('/sales details for <_id>')
def single_sales_details(_id):
    sales = Sales.query.filter_by(item_sold=_id).all()
    items = query_all(Items)
    return render_template("single_sales_details.html", sales=sales,items = items)


@dashboard_blueprint.route('/purchases summery')
def purchases_summery():
    purchases = query_all(Purchases)
    items = query_all(Items)
    price = {}
    quantity = {}

    for purchase in purchases:
        if purchase.item_purchased in price.keys():
            price[purchase.item_purchased] += purchase.quantity_purchased * purchase.unit_price
        else:
            price[purchase.item_purchased] = purchase.quantity_purchased * purchase.unit_price


    for purchase in purchases:
        if purchase.item_purchased in quantity.keys():
            quantity[purchase.item_purchased] += purchase.quantity_purchased
        else:
            quantity[purchase.item_purchased] = purchase.quantity_purchased

    return render_template("purchases_summery.html", price=price, quantity=quantity, items=items, purchases =purchases)


@dashboard_blueprint.route('/purchases details for <_id>')
def single_purchases_details(_id):
    purchases = Purchases.query.filter_by(item_purchased=_id).all()
    items = query_all(Items)
    return render_template("single_purchases_summery.html", purchases = purchases,items = items)