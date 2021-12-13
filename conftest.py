import pytest

from actors.user import User


@pytest.fixture(scope="function")
def user():
    return User(first_name="James", last_name="Lewis", email="james@gmail.com", password="P@ss1234")
