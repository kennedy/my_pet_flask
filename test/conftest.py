import pytest
import tempfile
from clicky import create_app


@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "DEBUG": True,
        "ENV": "development",
        "DATABASE": 'file::memory:?cache=shared'
    }
    app = create_app(test_config)
    yield app


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client
