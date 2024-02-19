"""
CRUD -
Get booking done in previous files.
Headers section --> Accept if not selected then it gives error as I am teapot(means not able to understand)

Create booking - POST request - requires - [ url, payload/ body(Json), headers, verify booking id, booking info(json)

"""
import requests
import pytest

pytest.mark.positive
def test_create_Booking_positive():
    print("Create booking Positive testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Swap",
        "lastname": "M",
        "totalprice": 777,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(response.json())
    print(type(json_payload))
    print(type(headers))
    print(type(response))  # provide us the created booking details
    data = response.json()
    print(type(data))

    # assertions
    assert response.status_code == 200, 'status code is incorrect'
    assert data["bookingid"] is not None
    assert data["booking"]["depositpaid"] == True
    assert data["booking"]["firstname"] is not "Jim"
    assert data["booking"]["bookingdates"]["checkin"] != data["booking"]["bookingdates"]["checkout"]


@pytest.mark.negative
def test_create_Booking_negative():
    print("Negative test case")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response_body = requests.post(url=URL, headers=headers, json=json_payload)

    print(type(response_body))
    assert response_body.status_code == 500



