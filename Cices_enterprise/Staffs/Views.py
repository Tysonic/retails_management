from Cices_enterprise.Staffs.Forms import AddStaff
from Cices_enterprise.Modules.Staffs import Staffs
from flask import render_template, redirect, url_for, flash, Blueprint
from Cices_enterprise import db

staffs_blueprint = Blueprint('Staffs', __name__, template_folder="templates/staffs")
@staffs_blueprint.route('/staffs/add new staff', methods=['GET','POST'])
def add_staff():
    form = AddStaff()
    if form.validate_on_submit():
        new_staff = Staffs(user_name=form.user_name.data, first_name=form.first_name.data,
                           other_name=form.other_name.data, home_address=form.address.data,
                           next_of_kin=form.next_of_kin.data,telephone_contact=form.tel.data,
                            role=form.role.data,
                           email=form.email.data)
        db.session.add(new_staff)
        db.session.commit()
        return redirect(url_for('Staffs.list_of_staffs'))
    return render_template("add_staffs.html", form=form)

@staffs_blueprint.route("/staffs/list of staffs")
def list_of_staffs():
    form = AddStaff()
    staffs = Staffs.query.all()
    return render_template("staffs.html", staffs=staffs, form=form)
