import os
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from dotenv import load_dotenv

load_dotenv()


app_dir = os.path.dirname(os.path.abspath(__file__))


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()
mail = Mail()


def create_app(config_name: str | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.DevelopmentConfig")
    if config_name == "production":
        app.config.from_object("config.ProductionConfig")
    elif config_name == "testing":
        app.config.from_object("config.TestingConfig")

    app.config.setdefault("SQLALCHEMY_DATABASE_URI", app.config.get("SQLALCHEMY_DATABASE_URI"))
    app.config.setdefault("UPLOAD_FOLDER", os.path.join(app.root_path, "uploads"))
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "warning"

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.models import User
        return db.session.get(User, int(user_id))

    from app.models.models import User

    with app.app_context():
        from app.models import models  # noqa: F401
        db.create_all()
        from app.utils.seed import seed_sample_data
        seed_sample_data()

    from app.auth.routes import auth_bp
    from app.admin.routes import admin_bp
    from app.donor.routes import donor_bp
    from app.inventory.routes import inventory_bp
    from app.request.routes import request_bp
    from app.hospital.routes import hospital_bp
    from app.reports.routes import reports_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(donor_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(request_bp)
    app.register_blueprint(hospital_bp)
    app.register_blueprint(reports_bp)

    @app.route("/")
    def index():
        if current_user.is_authenticated:
            return redirect(url_for("admin.dashboard"))
        return redirect(url_for("auth.login"))

    return app
