from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField


class AddItem(FlaskForm):
    item = StringField("Item")
    size = IntegerField("Size")
    unit = StringField("Units")
    packaging = StringField("Packaging")

    submit = SubmitField("Save")