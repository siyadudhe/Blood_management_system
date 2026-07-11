from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.forms.forms import BloodUnitForm
from app.models.models import BloodUnit

inventory_bp = Blueprint("inventory", __name__, template_folder="../templates")


@inventory_bp.route("/inventory")
@login_required
def inventory():
    units = BloodUnit.query.order_by(BloodUnit.created_at.desc()).all()
    return render_template("inventory/inventory.html", units=units)


@inventory_bp.route("/inventory/add", methods=["GET", "POST"])
@login_required
def add_stock():
    form = BloodUnitForm()
    if form.validate_on_submit():
        unit = BloodUnit(blood_group=form.blood_group.data, units=form.units.data, expiry_date=form.expiry_date.data, status=form.status.data, source=form.source.data or "manual")
        db.session.add(unit)
        db.session.commit()
        flash("Blood unit added", "success")
        return redirect(url_for("inventory.inventory"))
    return render_template("inventory/add_stock.html", form=form)


@inventory_bp.route("/inventory/edit/<int:unit_id>", methods=["GET", "POST"])
@login_required
def edit_stock(unit_id):
    unit = BloodUnit.query.get_or_404(unit_id)
    form = BloodUnitForm(obj=unit)
    if form.validate_on_submit():
        unit.blood_group = form.blood_group.data
        unit.units = form.units.data
        unit.expiry_date = form.expiry_date.data
        unit.status = form.status.data
        unit.source = form.source.data or unit.source
        db.session.commit()
        flash("Stock updated", "success")
        return redirect(url_for("inventory.inventory"))
    return render_template("inventory/edit_stock.html", form=form, unit=unit)
