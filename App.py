from Cices_enterprise import App
from flask import render_template


@App.route("/")
def index():
    return render_template("index.html")

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
