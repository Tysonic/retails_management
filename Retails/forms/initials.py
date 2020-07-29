from flask_wtf import  FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField


class AddInitials(FlaskForm):
    item_name = SelectField(label="Item",coerce=int)
    sales_quantity  = IntegerField("Sales Quantity")
    cash = IntegerField("Cash Amount")
    submit = SubmitField("Submit")