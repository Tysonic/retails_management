import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

login_manager = LoginManager()
App = Flask(__name__,template_folder='templates/shared')
login_manager.init_app(App)
basedir = os.path.abspath(os.path.dirname(__file__))
App.config["SECRET_KEY"] = "This is enterprise"
App.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# App.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "RetailsDB")
App.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(App)
Migrate(App, db)
Bootstrap(App)
login_manager.login_view = "accounts.login"

from Retails.views.items import items_blueprint
from Retails.views.sales import sales_blueprint
from Retails.views.stocks import purchase_blueprint
from Retails.views.staffs import staffs_blueprint
from Retails.views.dashboard import dashboard_blueprint
from Retails.views.accounts import accounts_blueprint
from Retails.views.initials import initials_blueprint



App.register_blueprint(items_blueprint, url_prifix="/items")
App.register_blueprint(staffs_blueprint, url_prifix='/staffs')
App.register_blueprint(purchase_blueprint, url_prifix='/stocks')
App.register_blueprint(sales_blueprint, url_prifix='/sales')
App.register_blueprint(initials_blueprint, url_prifix='/initials')
App.register_blueprint(dashboard_blueprint, url_prifix='/dashboard')
App.register_blueprint(accounts_blueprint,url_prifix='/accounts')
