import re
from Cices_enterprise.Modules.Users import Users
from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo


class UserRegitrationForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired(message="User Name required")])
    email = StringField("Email", validators=[DataRequired(message="Email Required"), Email()])
    password = PasswordField("Password",
                             validators=[DataRequired(message="Enter password"), EqualTo("confirm_password")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(message="Please confirm password")])

    submit = SubmitField("Register")

    def check_email(self, field):
        if Users.query.filter_by(self.email == field.data).first():
            raise ValidationError(message="your email has already been registered")

    def check_username(self, field):
        if Users.query.filter_by(self.username == field.data).first():
            raise ValidationError(message="Username already exitst")

    def check_password(self, field):
        if len(field.password < 8):
            raise ValidationError(message="Password must be at least 8 characters long")
        if not re.search(r"[\d]+", field.password):
            raise ValidationError(message="This password must contain at least 1 digit")
        if re.search(r"[A-Z]+", field.password.data):
            raise ValidationError("This password must contain at least 1 uppercase characte")


class UserLoginForm(FlaskForm):
    email = StringField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Login")
