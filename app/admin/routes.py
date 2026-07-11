from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.models import User, UserRole, Donor, Donation, BloodUnit, Hospital, BloodRequest
from app.forms.forms import DonorForm, BloodUnitForm, HospitalForm, BloodRequestForm, ProfileForm, ChangePasswordForm
from werkzeug.utils import secure_filename
import os

admin_bp = Blueprint("admin", __name__, template_folder="../templates")


@admin_bp.route("/dashboard")
@login_required
def dashboard():
    total_donors = Donor.query.count()
    total_units = db.session.query(db.func.sum(BloodUnit.units)).scalar() or 0
    pending_requests = BloodRequest.query.filter_by(status="pending").count()
    recent_donations = Donation.query.order_by(Donation.created_at.desc()).limit(5).all()
    blood_units = BloodUnit.query.order_by(BloodUnit.created_at.desc()).all()
    hospitals = Hospital.query.count()
    return render_template("admin/dashboard.html", total_donors=total_donors, total_units=total_units, pending_requests=pending_requests, recent_donations=recent_donations, blood_units=blood_units, hospitals=hospitals)


@admin_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.full_name = form.full_name.data
        current_user.email = form.email.data.lower()
        current_user.phone = form.phone.data
        current_user.address = form.address.data
        if form.profile_picture.data:
            filename = secure_filename(form.profile_picture.data.filename)
            path = os.path.join(current_user.id, filename)
            os.makedirs(os.path.dirname(os.path.join("app/uploads", path)), exist_ok=True)
            form.profile_picture.data.save(os.path.join("app/uploads", path))
            current_user.profile_picture = path
        db.session.commit()
        flash("Profile updated", "success")
        return redirect(url_for("admin.profile"))
    return render_template("admin/profile.html", form=form)


@admin_bp.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if not current_user.check_password(form.current_password.data):
            flash("Current password is incorrect", "danger")
        else:
            current_user.set_password(form.new_password.data)
            db.session.commit()
            flash("Password changed", "success")
            return redirect(url_for("admin.profile"))
    return render_template("admin/change_password.html", form=form)
