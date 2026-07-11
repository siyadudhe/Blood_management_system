import os
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db, csrf
from app.forms.forms import LoginForm, RegisterForm, ForgotPasswordForm, ResetPasswordForm
from app.models.models import User, UserRole

auth_bp = Blueprint("auth", __name__, template_folder="../templates")


@auth_bp.route("/login", methods=["GET", "POST"])
@csrf.exempt
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))
    form = LoginForm(meta={"csrf": False})
    if request.method == "POST":
        if form.validate():
            user = User.query.filter_by(email=form.email.data.lower()).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember.data)
                flash("Welcome back!", "success")
                return redirect(url_for("admin.dashboard"))
            flash("Invalid email or password", "danger")
        else:
            flash("Please correct the form errors and try again.", "warning")
    return render_template("auth/login.html", form=form)


@auth_bp.route("/register", methods=["GET", "POST"])
@csrf.exempt
def register():
    form = RegisterForm(meta={"csrf": False})
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user:
            flash("Email already registered", "warning")
        else:
            user = User(full_name=form.full_name.data, email=form.email.data.lower(), role=form.role.data, email_verified=True)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Registration successful. Please log in.", "success")
            return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))


@auth_bp.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    form = ForgotPasswordForm(meta={"csrf": False})
    if request.method == "POST" and form.validate():
        flash("If the account exists, a reset link has been sent.", "info")
        return redirect(url_for("auth.login"))
    return render_template("auth/forgot_password.html", form=form)


@auth_bp.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    form = ResetPasswordForm(meta={"csrf": False})
    if request.method == "POST" and form.validate():
        flash("Password updated successfully.", "success")
        return redirect(url_for("auth.login"))
    return render_template("auth/reset_password.html", form=form, token=token)
