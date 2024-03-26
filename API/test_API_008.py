import requests
import pytest


def test_unicorn():
    url = ("http://35.179.62.210/api/create_user")
    # Headers without Content-Type; let requests handle it
    headers = {}
    payload = {
        "full_name": "swapnali",
        "email": "swapnali@yopmail.com",
        "password": "Pass@123",
        "password_confirmation": "Pass@123",
        "mobile_number": "9876543212",
        "is_terms_accepted": "1"
    }

    # Use data for non-file fields in multipart/form-data
    response = requests.post(url=url, headers=headers, data=payload)
    print(response.text)
    data = response.json()
    print(data)

    assert data["status_code"] == 200,"error"
    assert data["data"]["user_id"] == 31, "wrong user id given"
    assert data["status"] != "false", "error 3"
    assert data["message"] != "OTP send"
