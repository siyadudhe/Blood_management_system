from flask import Blueprint, render_template, send_file, request
from flask_login import login_required
from io import BytesIO
from reportlab.pdfgen import canvas
import openpyxl
from app.models.models import Donation, BloodUnit, BloodRequest

reports_bp = Blueprint("reports", __name__, template_folder="../templates")


@reports_bp.route("/reports")
@login_required
def reports():
    donations = Donation.query.all()
    units = BloodUnit.query.all()
    requests = BloodRequest.query.all()
    return render_template("reports/reports.html", donations=donations, units=units, requests=requests)


@reports_bp.route("/reports/export/pdf")
@login_required
def export_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Vital Ledger Blood Bank Report")
    p.drawString(100, 780, "Generated from live database")
    p.save()
    buffer.seek(0)
    return send_file(buffer, mimetype="application/pdf", as_attachment=True, download_name="report.pdf")


@reports_bp.route("/reports/export/excel")
@login_required
def export_excel():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Inventory"
    sheet.append(["Blood Group", "Units", "Expiry Date", "Status"])
    for unit in BloodUnit.query.all():
        sheet.append([unit.blood_group, unit.units, unit.expiry_date, unit.status])
    buffer = BytesIO()
    workbook.save(buffer)
    buffer.seek(0)
    return send_file(buffer, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", as_attachment=True, download_name="inventory.xlsx")
