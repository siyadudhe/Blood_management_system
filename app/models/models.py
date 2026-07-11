from __future__ import annotations

from datetime import datetime, date
from enum import Enum
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class UserRole(str, Enum):
    ADMIN = "admin"
    STAFF = "staff"
    DONOR = "donor"


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default=UserRole.DONOR.value)
    phone = db.Column(db.String(30))
    address = db.Column(db.Text)
    profile_picture = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    email_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    donor_profile = db.relationship("Donor", back_populates="user", uselist=False)
    hospital = db.relationship("Hospital", back_populates="user", uselist=False)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class Donor(db.Model):
    __tablename__ = "donors"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    blood_group = db.Column(db.String(10), nullable=False)
    date_of_birth = db.Column(db.Date)
    last_donation_date = db.Column(db.Date)
    eligibility_status = db.Column(db.String(30), default="eligible")
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="donor_profile")
    donations = db.relationship("Donation", back_populates="donor", cascade="all, delete-orphan")
    requests = db.relationship("BloodRequest", back_populates="donor", cascade="all, delete-orphan")


class Donation(db.Model):
    __tablename__ = "donations"

    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey("donors.id"), nullable=False)
    donation_date = db.Column(db.Date, default=date.today)
    blood_group = db.Column(db.String(10), nullable=False)
    units = db.Column(db.Integer, nullable=False, default=1)
    status = db.Column(db.String(30), default="completed")
    certificate_file = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    donor = db.relationship("Donor", back_populates="donations")


class BloodUnit(db.Model):
    __tablename__ = "blood_units"

    id = db.Column(db.Integer, primary_key=True)
    blood_group = db.Column(db.String(10), nullable=False)
    units = db.Column(db.Integer, nullable=False, default=0)
    expiry_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(30), default="available")
    source = db.Column(db.String(50), default="donation")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Hospital(db.Model):
    __tablename__ = "hospitals"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    name = db.Column(db.String(120), nullable=False)
    license_number = db.Column(db.String(50))
    address = db.Column(db.Text)
    phone = db.Column(db.String(30))
    contact_person = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="hospital")
    requests = db.relationship("BloodRequest", back_populates="hospital", cascade="all, delete-orphan")


class BloodRequest(db.Model):
    __tablename__ = "blood_requests"

    id = db.Column(db.Integer, primary_key=True)
    hospital_id = db.Column(db.Integer, db.ForeignKey("hospitals.id"), nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey("donors.id"))
    blood_group = db.Column(db.String(10), nullable=False)
    units_required = db.Column(db.Integer, nullable=False, default=1)
    urgency = db.Column(db.String(20), default="normal")
    status = db.Column(db.String(20), default="pending")
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    hospital = db.relationship("Hospital", back_populates="requests")
    donor = db.relationship("Donor", back_populates="requests")


class ReportExport(db.Model):
    __tablename__ = "report_exports"

    id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.String(50), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
