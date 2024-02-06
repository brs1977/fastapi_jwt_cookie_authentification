import pytest
from fastapi_auth.model import User

valid_request_data = {"username": "test", "password": "test"}
invalid_request_data = {"username": "test", "password": "tes"}

def login(test_app, request_data):
    data = User(**request_data).model_dump_json()
    return test_app.post('login', data=data)


def test_login_valid(test_app):
    response = login(test_app, valid_request_data)
    assert response.status_code == 200
    assert 'access_token_cookie' in response.cookies
    assert 'refresh_token_cookie' in response.cookies

def test_login_invalid(test_app):
    response = login(test_app, invalid_request_data)
    assert response.status_code == 401

def test_protected_forbidden(test_app):
    test_app.delete('logout')

    response = test_app.get('protected')
    assert response.status_code == 401

def test_protected(test_app):
    login(test_app, valid_request_data)

    response = test_app.get('protected')
    assert response.status_code == 200


@pytest.mark.freeze_time('2023-01-01')
def test_login_forbidden_with_expired_token(test_app, freezer):
    response = login(test_app, valid_request_data)

    freezer.move_to('2024-01-01')
    response = test_app.get('protected')
    assert response.text == '{"detail":"Signature has expired"}'
