from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

class AddImage(FlaskForm):
    image = FileField("Select image to upload")
    submit = SubmitField("Upload")
