from flask_wtf import  FlaskForm
from wtforms import IntegerField, SubmitField, StringField, SelectField


class AddInitials(FlaskForm):
    item_name = SelectField(label="Item",coerce=int)
    quantity  = IntegerField("Quantity")
    cash = IntegerField("Cash")
    submit = SubmitField("Submit")