import pytest
from app1 import app  # Hier wird die Flask-App importiert. Passe den Pfad je nach Verzeichnisstruktur an.


@pytest.fixture
def client():
    # Fixture, die einen Test-Client für Flask zurückgibt
    with app.test_client() as client:
        yield client


def test_hello(client):
    # Test für die Route '/'
    response = client.get('/')

    # Überprüfen, ob der Statuscode 200 ist (OK)
    assert response.status_code == 200

    # Überprüfen, ob der Inhalt der Antwort den Text "Hello, DevSecOps!" enthält
    assert b'Hello, DevSecOps!' in response.data