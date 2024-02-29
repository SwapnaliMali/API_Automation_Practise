import requests
import pytest

# Create token API

pytest.mark.positive

def test_create_token_positive():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response_body = requests.post(url=URL, headers=headers, json=payload)
    print(type(response_body))
    print(response_body.json())
    print(response_body.content)

    assert response_body.json() != 0


pytest.mark.negative
def test_create_token_negative():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {}
    #     payload ={
    #     "username" : "admin",
    #     "password" : "password123"
    # }
    response_body = requests.post(url=URL, headers=headers, json=payload)
    print(type(response_body))
    print(response_body.json())
    print(response_body.content)

    assert response_body.status_code == 200


# Put request to update full booking details

def create_token():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response_body = requests.post(url=URL, headers=headers, json=payload)
    print(type(response_body))
    print(response_body.json())
    print(response_body.content)
    data = response_body.json()
    token = data["token"]
    print(token)
    return token


def test_update_booking():
    URL = "https://restful-booker.herokuapp.com/booking/11"
    Cookie = "token=" + create_token()
    headers = {
        "Content-type": "application/json",

        "Cookie": Cookie
    }
    payload = {
        "firstname": "Swap",
        "lastname": "M",
        "totalprice": 554,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-02-19",
            "checkout": "2024-11-03"
        }
    }

    response_body = requests.put(url=URL, headers=headers, json=payload)
    data = response_body.json()
    print(data)

    assert data["firstname"] == "Swap","Incorrect name"
    assert response_body.status_code == 200


# Delete booking

# def test_delete_booking():
#     url = "https://restful-booker.herokuapp.com/booking/1"
#     Cookie = "token=" + create_token()
#     headers = {
#         "Content-type": "application/json",
#
#         "Cookie": Cookie
#     }
#     response_data = requests.delete(url=url,headers=headers)
#     data = response_data
#     print(data)
#     assert response_data.status_code == 201


def test_patch_booking():
    URL = "https://restful-booker.herokuapp.com/booking/1"
    Cookie = "token=" + create_token()
    headers = {
        "Content-type": "application/json",

        "Cookie": Cookie
    }
    payload = {
        "firstname": "Swap",
        "lastname": "M",
        "totalprice": 554,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-02-19",
            "checkout": "2024-11-03"
        }
    }

    response_body = requests.patch(url=URL, headers=headers, json=payload)
    data = response_body.json()
    print(data)