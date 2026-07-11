from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.forms.forms import BloodRequestForm
from app.models.models import BloodRequest, Hospital

request_bp = Blueprint("request", __name__, template_folder="../templates")


@request_bp.route("/requests")
@login_required
def requests():
    requests = BloodRequest.query.order_by(BloodRequest.created_at.desc()).all()
    return render_template("request/requests.html", requests=requests)


@request_bp.route("/requests/new", methods=["GET", "POST"])
@login_required
def new_request():
    form = BloodRequestForm()
    if form.validate_on_submit():
        hospital = Hospital.query.first()
        req = BloodRequest(hospital_id=hospital.id, blood_group=form.blood_group.data, units_required=form.units_required.data, urgency=form.urgency.data, notes=form.notes.data)
        db.session.add(req)
        db.session.commit()
        flash("Request created", "success")
        return redirect(url_for("request.requests"))
    return render_template("request/new_request.html", form=form)


@request_bp.route("/requests/<int:request_id>/status/<status>", methods=["POST"])
@login_required
def update_status(request_id, status):
    req = BloodRequest.query.get_or_404(request_id)
    req.status = status
    db.session.commit()
    flash("Request updated", "success")
    return redirect(url_for("request.requests"))
