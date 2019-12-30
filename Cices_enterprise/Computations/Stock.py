# import os
#
# from Cices_enterprise import basedir
#
#
# def stock():
#     from sqlalchemy import  create_engine
#     engine = create_engine('sqlite:///'+ os.path.join(basedir, "CiceDB"))
#     with engine.connect() as con:
#         items = con.execute("select item, stock, quantity_purchased, quantity_sold from Items inner join Purchases on Items._Id=Purchases.item_purchased inner join Sales on Items._Id=Sales.item_sold").fetchall()
#
#     stock_dict = {}
#
#     for x in items:
#         if x.item in stock_dict.keys():
#             stock_dict[x.item] =stock_dict.values()+x.quantity_purchased-x.quantity_sold+ x.stock
#         else:
#             stock_dict[x.item]=x.quantity_purchased-x.quantity_sold+ x.stock
#     return stock_dict
#
# y = stock()
# print(y)