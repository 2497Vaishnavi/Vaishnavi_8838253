# integration_test.py

from login import login

def test_successful_login():
    assert login("user", "password") == True

def test_failed_login():
    assert login("invalid_user", "invalid_password") == False
