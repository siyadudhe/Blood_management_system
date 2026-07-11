from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.forms.forms import HospitalForm
from app.models.models import Hospital

hospital_bp = Blueprint("hospital", __name__, template_folder="../templates")


@hospital_bp.route("/hospitals")
@login_required
def hospitals():
    hospitals = Hospital.query.all()
    return render_template("hospital/hospitals.html", hospitals=hospitals)


@hospital_bp.route("/hospitals/add", methods=["GET", "POST"])
@login_required
def add_hospital():
    form = HospitalForm()
    if form.validate_on_submit():
        hospital = Hospital(name=form.name.data, license_number=form.license_number.data, address=form.address.data, phone=form.phone.data, contact_person=form.contact_person.data)
        db.session.add(hospital)
        db.session.commit()
        flash("Hospital added", "success")
        return redirect(url_for("hospital.hospitals"))
    return render_template("hospital/add_hospital.html", form=form)
