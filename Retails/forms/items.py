from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField


class AddItem(FlaskForm):
    name = StringField('Name')
    unit_stock= StringField('Unit Stock')
    unit_sales = StringField('Unit Sales')
    sales_per_stock = IntegerField('Sales Per Stock')
    size = StringField('Size')
    category = StringField('Category')
    selling_price = IntegerField("Selling Price")
    buying_price = IntegerField("Buying Price")
    archived = BooleanField("Archived")
    company = StringField("Company")
    submit = SubmitField("Save")