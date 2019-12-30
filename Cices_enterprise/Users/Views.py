import re

from flask import render_template, redirect, flash, url_for, request
from werkzeug.security import check_password_hash
from flask_login import login_required, login_user, logout_user
from wtforms import ValidationError

from Cices_enterprise import login_manager, App, db
from Cices_enterprise.Users.Forms import UserLoginForm, UserRegitrationForm
from Cices_enterprise.Modules.Users import Users
from flask import Blueprint

users_blueprint = Blueprint("Users", __name__, template_folder='templates/users')


@users_blueprint.route("/login page", methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    try:
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user is not None and check_password_hash(user.password_hash, form.password.data) :

                login_user(user)
                flash("logged in successfully")
                next = request.args.get("next")

                if next == None or not next[0] == '/':
                    next = url_for("welcome")
            else:
                raise ValidationError("Password or username is incorrect ")
            return redirect(next)

        return render_template("login.html", form=form)
    except Exception as e:

        return render_template("login.html", form=form, error =e)


@users_blueprint.route("/logout user")
@login_required
def logout():
    logout_user()
    flash("logged out successfully")
    return redirect(url_for("index"))


@users_blueprint.route("/registration page", methods=["GET", "POST"])
def register():
    form = UserRegitrationForm()
    try:

        if form.validate_on_submit():

            if Users.query.filter_by(email=form.email.data).first():
                raise ValidationError("your email has already been registered")
            if Users.query.filter_by(username=form.username.data).first():
                raise ValidationError("The User Name has already been taken Please Choose another name")
            if len(form.password.data)<8:
                raise ValidationError("Password must be at least 8 characters long")
            if not re.search(r"[\d]+", form.password.data):
                raise ValidationError("This password must contain at least 1 digit")
            if not re.search(r"[A-Z]+", form.password.data):
                print(form.password.data)
                raise ValidationError("This password must contain at least 1 uppercase character")

            new_user = Users(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash("Registered successfully  ")
            return redirect(url_for("Users.login"))
        return render_template("register.html", form=form)
    except Exception as e:
        return render_template("register.html", error=e, form=form)
