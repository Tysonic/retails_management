from flask_login import login_required
from Retails import App, login_manager
from flask import render_template
from Retails.modules.Accounts import Accounts


@login_manager.user_loader
def load_user(user_id):
    return Accounts.query.get(user_id)


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



# @App.errorhandler(200)
# def Internal_server_error(e):
# 	return render_template("200.html",error=e)



if __name__ == "__main__":
    App.run(debug=True)
