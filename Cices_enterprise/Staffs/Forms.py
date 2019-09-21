from wtforms import SubmitField, SelectField, StringField, IntegerField, DateTimeField
from flask_wtf import FlaskForm
class AddStaff(FlaskForm):
    user_name = StringField('User Name')
    first_name = StringField('First Name')
    other_name = StringField('Other Name')
    address = StringField('Home Address')
    next_of_kin = StringField("Next of Kin")
    birthday = DateTimeField('Date of Birth')
    role = StringField("Role")
    tel = StringField('Phone Contact')
    email = StringField('Email')
    submit = SubmitField("Register")