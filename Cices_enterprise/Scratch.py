from Cices_enterprise.Computations.Query import query_one
from Cices_enterprise.Modules import ItemDetails
from Cices_enterprise.Modules.Items import Items
from Cices_enterprise import db
from Cices_enterprise.Modules.Purchases import Purchases
from Cices_enterprise.Modules.Sales import Sales
from Cices_enterprise.Modules.Users import Users



sales = Sales.query.filter_by(item_sold=1).all()

for sale in sales :
    print(sale)




