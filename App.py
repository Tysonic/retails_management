from flask_login import login_required

from Cices_enterprise import App, login_manager
from flask import render_template

from Cices_enterprise.Modules.Users import Users


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

@App.route("/")
def index():
    return render_template("index.html")


@App.route("/welcome page", methods=['GET', 'POST'])
@login_required
def welcome():
    return render_template("welcome.html")


@App.errorhandler(404)
def page_not_found(e):
	return render_template("404.html",error=e)

@App.errorhandler(500)
def Internal_server_error(e):
	return render_template("500.html",error=e)

# @App.errorhandler(200)
# def Internal_server_error(e):
# 	return render_template("200.html",error=e)



if __name__ == "__main__":
    App.run(debug=True)
