from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddItem(FlaskForm):
    name = StringField('Name')
    unit_stock= StringField('Unit Stock')
    unit_sales = StringField('Unit Sales')
    sales_per_stock = IntegerField('Sales Per Stock')
    size = StringField('Size')
    category = StringField('Category')
    submit = SubmitField("Save")