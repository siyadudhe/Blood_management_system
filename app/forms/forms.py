from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SelectField, IntegerField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired(), Length(min=2, max=120)])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    role = SelectField("Role", choices=[("donor", "Donor"), ("staff", "Staff"), ("admin", "Admin")], default="donor")
    submit = SubmitField("Create Account")


class ForgotPasswordForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Send Reset Link")


class ResetPasswordForm(FlaskForm):
    password = PasswordField("New Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Reset Password")


class DonorForm(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone")
    address = TextAreaField("Address")
    blood_group = SelectField("Blood Group", choices=[("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")])
    date_of_birth = DateField("Date of Birth", validators=[Optional()])
    notes = TextAreaField("Notes")
    submit = SubmitField("Save Donor")


class BloodUnitForm(FlaskForm):
    blood_group = SelectField("Blood Group", choices=[("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")])
    units = IntegerField("Units", validators=[DataRequired()])
    expiry_date = DateField("Expiry Date", validators=[DataRequired()])
    status = SelectField("Status", choices=[("available", "Available"), ("low", "Low"), ("expired", "Expired")])
    source = StringField("Source")
    submit = SubmitField("Save Unit")


class BloodRequestForm(FlaskForm):
    blood_group = SelectField("Blood Group", choices=[("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")])
    units_required = IntegerField("Units Required", validators=[DataRequired()])
    urgency = SelectField("Urgency", choices=[("normal", "Normal"), ("urgent", "Urgent"), ("emergency", "Emergency")])
    notes = TextAreaField("Notes")
    submit = SubmitField("Create Request")


class HospitalForm(FlaskForm):
    name = StringField("Hospital Name", validators=[DataRequired()])
    license_number = StringField("License Number")
    address = TextAreaField("Address")
    phone = StringField("Phone")
    contact_person = StringField("Contact Person")
    submit = SubmitField("Save Hospital")


class ProfileForm(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    phone = StringField("Phone")
    address = TextAreaField("Address")
    profile_picture = FileField("Profile Picture", validators=[FileAllowed(["jpg", "jpeg", "png", "gif"], "Images only!")])
    submit = SubmitField("Update Profile")


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField("Current Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("new_password")])
    submit = SubmitField("Change Password")
