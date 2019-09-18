from Cices_enterprise import App
from flask import render_template


@App.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    App.run(debug=True)
