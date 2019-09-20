from Cices_enterprise.Staffs.Forms import AddStaff
from Cices_enterprise.Modules.Staffs import Staffs
from flask import render_template, redirect, url_for, flash, Blueprint
from Cices_enterprise import db

staffs_blueprint = Blueprint('Staffs', __name__, template_folder="templates/staffs")
@staffs_blueprint.route('/staffs/add new staff')
def add_staff():
    form = AddStaff()
    if form.validate_on_submit():
        new_staff = Staffs(user_name = form.user_name.data, first_name=form.first_name.data,
                           other_name=form.other_name.data, home_address=form.address.data,
                           next_of_kin=form.next_of_kin.data,telephone_contact=form.tel.data,
                           date_of_birth=form.birthday.data, role=form.role.data,
                           email=form.email.data)
        db.session.add(new_staff)
        db.session.commit()
        return redirect(url_for('staffs.html'))
    return render_template("add_staffs.html")

@staffs_blueprint.route("/staffs/list of staffs")
def list_of_staffs():
    form = AddStaff()
    staffs = Staffs.query.all()
    return render_template("staff.html", staffs=staffs, form=form)
