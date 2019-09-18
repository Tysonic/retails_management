import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


App = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
App.config["SECRET_KEY"]="This is tysonic enterprise"
App.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
App.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'Cice_shoppers.db')
db = SQLAlchemy(App)
Migrate(App,db)

from Cices_enterprise.Items.Views import items_blueprint
App.register_blueprint(items_blueprint, url_prifix="/items")