from flask_login import login_required
from Retails import app, login_manager, db
from flask import render_template
from Retails.modules.Accounts import Accounts


@login_manager.user_loader
def load_user(user_id):
    return Accounts.query.get(user_id)



@app.route("/")
@app.route("/home")
@login_required
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", error=e)


@app.errorhandler(500)
def Internal_server_error(e):
    return render_template("500.html", error=e)



# @app.errorhandler(200)
# def Internal_server_error(e):
# 	return render_template("200.html",error=e)


@app.cli.command(name='create_tables')
def create_tables():
    db.create_all()


@app.cli.command(name='create_admin')
def create_admin():
    admin = Accounts(email='adminadd@gmail.com',password='adminadmin', username='admin')
    db.session.add(admin)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
