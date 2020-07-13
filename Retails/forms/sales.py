from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, IntegerField,DateTimeField


class AddSales(FlaskForm):
    item_sold = SelectField(label="Item", coerce=int)
    unit_price = IntegerField("Price")
    quantity_sold = IntegerField("Quantity")
    sold_on = DateTimeField("Sold on")
    sold_by = StringField("Sold By")
    recorded_at = DateTimeField("Recorded At")
    updated_by = StringField("Updated By")
    updated_at = DateTimeField("Updated At")
    submit = SubmitField("Save")
