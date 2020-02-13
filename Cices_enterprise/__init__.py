import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_bootstrap import Bootstrap

login_manager = LoginManager()
App = Flask(__name__)
login_manager.init_app(App)
basedir = os.path.abspath(os.path.dirname(__file__))
App.config["SECRET_KEY"] = "This is enterprise"
App.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
App.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "CiceDB")
App.config["SQLALCHEMY_BINDS"] = {"Accounts": "sqlite:///" + os.path.join(basedir, "AccountsDB")}
db = SQLAlchemy(App)
Migrate(App, db)
Bootstrap(App)
login_manager.login_view = "login"

from Cices_enterprise.Items.Views import items_blueprint
from Cices_enterprise.Sales.Views import sales_blueprint
from Cices_enterprise.Purchases.Views import purchase_blueprint
from Cices_enterprise.Staffs.Views import staffs_blueprint
from Cices_enterprise.Items.ItemDetails.ItemDetailsView import items_details_blueprint
from Cices_enterprise.Dashboard.Views import dashboard_blueprint

App.register_blueprint(staffs_blueprint, url_prifix='/staffs')
App.register_blueprint(purchase_blueprint, url_prifix='/purchases')
App.register_blueprint(sales_blueprint, url_prifix='/sales')
App.register_blueprint(items_blueprint, url_prifix="/items")
App.register_blueprint(items_details_blueprint, url_prifix="advanced")
App.register_blueprint(dashboard_blueprint, url_prifix='dashboard')
