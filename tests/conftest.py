
import pytest
from fastapi_auth.server import create_app
from starlette.testclient import TestClient

@pytest.fixture(scope="module")
def test_app():    
    with TestClient(create_app()) as client:  # context manager will invoke startup event
        yield client

@pytest.fixture
def api_url():
    def api_url_function(url):
        return url
        # return f"{settings.PROJECT_API_VERSION}/{url}"
    return api_url_function

