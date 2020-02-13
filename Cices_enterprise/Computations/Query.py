from Cices_enterprise.Modules.Purchases import Purchases
from Cices_enterprise.Modules.Sales import Sales


def query_all(table):
    return table.query.all()


def query_one(table, _id):
    return table.query.filter_by(_Id=_id)


