import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

App = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
App.config["SECRET_KEY"] = "This is tysonic enterprise"
App.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
App.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(basedir,"CiceDB")
App.config['IMAGE_UPLOADER'] = ".\Static\Images"
db = SQLAlchemy(App)
Migrate(App, db)
Bootstrap(App)

upload = os.path.join(basedir,App.config["IMAGE_UPLOADER"])
from Cices_enterprise.Items.Views import items_blueprint
from Cices_enterprise.Sales.Views import sales_blueprint
from Cices_enterprise.Purchases.Views import purchase_blueprint
from Cices_enterprise.Staffs.Views import staffs_blueprint
from Cices_enterprise.Uploaders.Uploader import uploader_blueprint
from Cices_enterprise.Modules.ItemImages import image_blueprint

App.register_blueprint(staffs_blueprint, url_prifix='/staffs')
App.register_blueprint(purchase_blueprint, url_prifix='/purchases')
App.register_blueprint(sales_blueprint, url_prifix='/sales')
App.register_blueprint(items_blueprint, url_prifix="/items")
App.register_blueprint(uploader_blueprint, url_prifix='uploader')
App.register_blueprint(image_blueprint, url_prifix='images')