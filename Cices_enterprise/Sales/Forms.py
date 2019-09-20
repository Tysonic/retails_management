from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, IntegerField,DateTimeField


class AddSales(FlaskForm):
    item = SelectField("Item")
    price = IntegerField("Price")
    quantity = IntegerField("Quantity")
    unit = SelectField("Unit")
    sold_on = DateTimeField("Sold on")
    submit = SubmitField("Save")
