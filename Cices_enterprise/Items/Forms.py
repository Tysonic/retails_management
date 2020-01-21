from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField, SelectField, FormField


class AddItem(FlaskForm):
    name = SelectField(label="Item", coerce=int)
    size = StringField("Size")
    unit = SelectField(label="Units", coerce=int)
    packaging = SelectField(label="Packaging", coerce=int)
    brand = SelectField(label="Brand", coerce=int)
    initial = IntegerField("Initial Value")
    submit = SubmitField("Save")
    update = SubmitField('Update')
