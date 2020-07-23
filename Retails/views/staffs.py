from Retails.forms.staffs import AddStaff
from Retails.modules.Staffs import Staffs
from flask import render_template, redirect, url_for, flash, Blueprint
from Retails import db

staffs_blueprint = Blueprint('staffs', __name__, template_folder="../templates/staffs")
@staffs_blueprint.route('/staffs/add new staff', methods=['GET','POST'])
def staff_add():
    form = AddStaff()
    if form.validate_on_submit():
        new_staff = Staffs(user_name=form.user_name.data, first_name=form.first_name.data,
                           other_name=form.other_name.data, home_address=form.address.data,
                           next_of_kin=form.next_of_kin.data,telephone_contact=form.tel.data,
                            role=form.role.data,
                           email=form.email.data)
        db.session.add(new_staff)
        db.session.commit()
        return redirect(url_for('staffs.list'))
    return render_template("add_staffs.html", form=form)

@staffs_blueprint.route("/staffs/list of staffs")
def staff_list():
    form = AddStaff()
    staffs = Staffs.query.all()
    return render_template("list_staffs.html", staffs=staffs, form=form)
