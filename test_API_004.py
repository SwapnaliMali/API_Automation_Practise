import pytest
import requests



#  Get the booking by id API request verify-


def test_get_booking_by_id():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1")
    print(response_body.url)
    print(response_body.status_code)
    print(response_body.json)
    data = response_body.json()
    print("Data : ",data)

    assert data["firstname"] == "Susan","Firstname is wrong"  #pass test case
    assert data["bookingdates"]["checkout"] != data["bookingdates"]["checkin"],"incorrect dates" #fail test case


