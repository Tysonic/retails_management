from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField

class AddImage(FlaskForm):
    image = FileField("Select image to upload")
    description = StringField("Description")
    submit = SubmitField("Upload")
