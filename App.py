import re

from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect
from wtforms import ValidationError

from Cices_enterprise import App, login_manager, db
from flask import render_template, request, url_for,flash
from Cices_enterprise.Modules.Users import Users
from Cices_enterprise.Users.Forms import UserLoginForm, UserRegitrationForm


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@App.route("/")
@App.route("/home")
@login_required
def index():
    return render_template("index.html")



@App.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", error=e)


@App.errorhandler(500)
def Internal_server_error(e):
    return render_template("500.html", error=e)




@App.route("/login page", methods=['GET', 'POST'])
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
                    next = url_for("index")
            else:
                raise ValidationError("Password or username is incorrect ")
            return redirect(next)

        return render_template("login.html", form=form)
    except Exception as e:

        return render_template("login.html", form=form, error =e)


@App.route("/logout user")
@login_required
def logout():
    logout_user()
    flash("logged out successfully")
    return redirect(url_for("index"))


@App.route("/registration page", methods=["GET", "POST"])
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


# @App.errorhandler(200)
# def Internal_server_error(e):
# 	return render_template("200.html",error=e)



if __name__ == "__main__":
    App.run(debug=True)
