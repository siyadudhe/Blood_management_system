from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from app.forms.forms import DonorForm
from app.models.models import User, Donor, Donation

donor_bp = Blueprint("donor", __name__, template_folder="../templates")


@donor_bp.route("/donors")
@login_required
def donors():
    donors = Donor.query.all()
    return render_template("donor/donors.html", donors=donors)


@donor_bp.route("/donors/add", methods=["GET", "POST"])
@login_required
def add_donor():
    form = DonorForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user:
            flash("Email already used", "warning")
        else:
            user = User(full_name=form.full_name.data, email=form.email.data.lower(), role="donor", email_verified=True)
            user.set_password("changeme")
            db.session.add(user)
            db.session.flush()
            donor = Donor(user_id=user.id, blood_group=form.blood_group.data, date_of_birth=form.date_of_birth.data, notes=form.notes.data)
            donor.user = user
            db.session.add(donor)
            db.session.commit()
            flash("Donor added", "success")
            return redirect(url_for("donor.donors"))
    return render_template("donor/add_donor.html", form=form)


@donor_bp.route("/donors/edit/<int:donor_id>", methods=["GET", "POST"])
@login_required
def edit_donor(donor_id):
    donor = Donor.query.get_or_404(donor_id)
    form = DonorForm(obj=donor.user)
    form.blood_group.data = donor.blood_group
    form.date_of_birth.data = donor.date_of_birth
    form.notes.data = donor.notes
    if form.validate_on_submit():
        donor.user.full_name = form.full_name.data
        donor.user.email = form.email.data.lower()
        donor.user.phone = form.phone.data
        donor.user.address = form.address.data
        donor.blood_group = form.blood_group.data
        donor.date_of_birth = form.date_of_birth.data
        donor.notes = form.notes.data
        db.session.commit()
        flash("Donor updated", "success")
        return redirect(url_for("donor.donors"))
    return render_template("donor/edit_donor.html", form=form, donor=donor)


@donor_bp.route("/donors/delete/<int:donor_id>", methods=["POST"])
@login_required
def delete_donor(donor_id):
    donor = Donor.query.get_or_404(donor_id)
    db.session.delete(donor.user)
    db.session.commit()
    flash("Donor deleted", "success")
    return redirect(url_for("donor.donors"))
