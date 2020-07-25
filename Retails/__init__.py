import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

login_manager = LoginManager()
app = Flask(__name__,template_folder='templates/shared')
login_manager.init_app(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SECRET_KEY"] = "This is enterprise"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "RetailsDB")
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Always Happy@localhost:5432/retailsdb"
db = SQLAlchemy(app)
Migrate(app, db)
Bootstrap(app)
login_manager.login_view = "accounts.login"

from Retails.views.items import items_blueprint
from Retails.views.sales import sales_blueprint
from Retails.views.stocks import purchase_blueprint
from Retails.views.staffs import staffs_blueprint
from Retails.views.dashboard import dashboard_blueprint
from Retails.views.accounts import accounts_blueprint
from Retails.views.initials import initials_blueprint



app.register_blueprint(items_blueprint, url_prifix="/items")
app.register_blueprint(staffs_blueprint, url_prifix='/staffs')
app.register_blueprint(purchase_blueprint, url_prifix='/stocks')
app.register_blueprint(sales_blueprint, url_prifix='/sales')
app.register_blueprint(initials_blueprint, url_prifix='/initials')
app.register_blueprint(dashboard_blueprint, url_prifix='/dashboard')
app.register_blueprint(accounts_blueprint,url_prifix='/accounts')
