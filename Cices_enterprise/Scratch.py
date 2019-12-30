from Cices_enterprise.Modules.Items import  Items
from Cices_enterprise import db



details = Items.query.filter_by(_Id = 1).first()
print(details.created_by)

