from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DateTimeField
from Cices_enterprise.Modules.Items import Items



def item_choises():
    item_list = []
    items = Items.query.all()
    for item in items:
        item_list.append((item.Id, item.name))
    return item_list

class AddPurchase(FlaskForm):
    item = SelectField(label="Item",coerce=int)
    price = IntegerField("Price")
    date = DateTimeField("Date")
    quantity = IntegerField("Quantity")
    submit = SubmitField("Save")