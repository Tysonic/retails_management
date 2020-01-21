from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DateTimeField
from Cices_enterprise.Modules.Items import Items

class AddPurchase(FlaskForm):
    item_purchased = SelectField(label="Item",coerce=int)
    unit_price = IntegerField("Price")
    quantity_purchased = IntegerField("Quantity Purchased")
    purchase_date = DateTimeField("Date Purchased")
    recorded_at = DateTimeField("Recorded At")
    purchased_by = StringField("Purchased by ")
    updated_at = DateTimeField("Updated At")
    updated_by = StringField("Updated By")
    submit = SubmitField("Save")
    update = SubmitField("Update")
