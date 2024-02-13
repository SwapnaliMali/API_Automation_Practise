import requests


#Verify --> asertion --> asssertion means verify if the actual & expected result matches

def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/21")
    print(response_body.json())
    print(response_body.url)
    data = response_body.json()
    print(data)
    assert response_body.status_code == 200  # if status code not equal to, means if not satisfied then only response given

    # assertions for other values of API
    assert 'firstname' in data, "firstname key is  present"
    assert 'totalprice' in data, "totalprice is present"
    assert 'depositpaid' in data, "depositpaid is true"
    assert data['firstname'] == 'John', "John is present" #Louis is present
    assert data["bookingdates"]["checkin"] == '2018-01-01','checkin date correct'

    assert data["bookingdates"]["checkout"] not




if __name__ == "__main__":
    main()