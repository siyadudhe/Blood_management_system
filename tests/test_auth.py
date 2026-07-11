import os
import tempfile

import pytest

from app import create_app, db


@pytest.fixture()
def client():
    app = create_app("testing")
    app.config.update(TESTING=True)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            from app.utils.seed import seed_sample_data
            seed_sample_data()
        yield client


def test_login_success(client):
    response = client.post(
        "/login",
        data={"email": "admin@vitalledger.local", "password": "admin123", "submit": "Login"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.request.path == "/dashboard"
