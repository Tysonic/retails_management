from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class Advanced(FlaskForm):
    item = StringField("Item ")
    unit = StringField("Unit")
    brand = StringField("Brand")
    packaging = StringField("Packaging")
    submit = SubmitField("Save")
    submit_all = SubmitField("Save all")



