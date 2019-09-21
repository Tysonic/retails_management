from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, IntegerField,DateTimeField


class AddSales(FlaskForm):
    item = StringField("Item")
    price = IntegerField("Price")
    quantity = IntegerField("Quantity")
    unit = StringField("Unit")
    sold_on = DateTimeField("Sold on")
    submit = SubmitField("Save")
