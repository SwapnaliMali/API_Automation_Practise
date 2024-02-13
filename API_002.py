import requests


#Verify --> asertion --> asssertion means verify if the actual & expected result matches

def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1")
    print(response_body.json())
    data = response_body.json()
    print(data)
    assert response_body.status_code == 200  # if status code not equal to, means if not satisfied then only response given

    # assertions for other values of API
    assert 'firstname' in data, "firstname key is  present"
   



if __name__ == "__main__":
    main()