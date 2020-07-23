from Retails.modules.Stocks import Stocks
from Retails.modules.Sales import Sales


def query_all(table):
    return table.query.all()


def query_one(table, _id):
    return table.query.filter_by(id=_id)


