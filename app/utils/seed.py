from app import db
from app.models.models import User, UserRole, Donor, Donation, BloodUnit, Hospital, BloodRequest
from datetime import date, timedelta


def seed_sample_data():
    if User.query.first():
        return

    admin = User(full_name="Dr. Sarah Vales", email="admin@vitalledger.local", role=UserRole.ADMIN.value, email_verified=True)
    admin.set_password("admin123")
    db.session.add(admin)

    staff = User(full_name="Dr. Michael Chen", email="staff@vitalledger.local", role=UserRole.STAFF.value, email_verified=True)
    staff.set_password("staff123")
    db.session.add(staff)

    donor = User(full_name="John Doe", email="donor@vitalledger.local", role=UserRole.DONOR.value, email_verified=True)
    donor.set_password("donor123")
    db.session.add(donor)
    db.session.flush()

    donor_profile = Donor(user_id=donor.id, blood_group="O+", date_of_birth=date(1990, 5, 12), last_donation_date=date.today() - timedelta(days=30), eligibility_status="eligible", notes="Regular donor")
    db.session.add(donor_profile)
    db.session.flush()

    db.session.add(Donation(donor_id=donor_profile.id, donation_date=date.today() - timedelta(days=30), blood_group="O+", units=1, status="completed"))
    db.session.add(BloodUnit(blood_group="A+", units=42, expiry_date=date.today() + timedelta(days=45), status="available"))
    db.session.add(BloodUnit(blood_group="O-", units=8, expiry_date=date.today() + timedelta(days=12), status="low"))
    db.session.add(BloodUnit(blood_group="B+", units=112, expiry_date=date.today() + timedelta(days=90), status="available"))
    db.session.add(BloodUnit(blood_group="AB+", units=15, expiry_date=date.today() + timedelta(days=30), status="available"))

    hospital = Hospital(user_id=staff.id, name="St. Jude Medical Center", license_number="LIC-1001", address="100 Care Avenue", phone="555-0100", contact_person="Nurse Maya")
    db.session.add(hospital)
    db.session.flush()

    db.session.add(BloodRequest(hospital_id=hospital.id, donor_id=donor_profile.id, blood_group="O-", units_required=4, urgency="emergency", status="pending", notes="Urgent surgery"))
    db.session.commit()
