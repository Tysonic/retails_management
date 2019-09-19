from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DateTimeField


class AddPurchase(FlaskForm):
    item = StringField("Item")
    price = IntegerField("Price")
    date = DateTimeField("Date")
    quantity = IntegerField("Quantity")
    submit = SubmitField("Save")