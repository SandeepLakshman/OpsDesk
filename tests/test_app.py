import pytest
from app import create_app, db


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()

        yield client

        with app.app_context():
            db.session.remove()
            db.drop_all()


def test_dashboard(client):
    response = client.get("/")
    assert response.status_code == 200


def test_incidents_page(client):
    response = client.get("/incidents")
    assert response.status_code == 200


def test_create_incident(client):
    response = client.post(
        "/incidents",
        data={
            "title": "Test incident",
            "description": "Testing incident creation",
            "priority": "High"
        },
        follow_redirects=True
    )

    assert response.status_code == 500
    assert b"Test incident" in response.data