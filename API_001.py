# API -> Requests library is an Http library used in Python for API Automation
# To make Http methods - CRUD methods, we need this requests library & to verify it we need Pytest
# What to verify in API request --> url, auth, headers, cookies, data(payload),json schema validation
# Python Testing frameworks - Pytest, Nose, Unit test
#every test case starts with test_,
# pytest -h  --> help
# pytest -k  --> match substring
# pytest -v --> verbose

import requests


#write the code here, learn this syntax of function & use the same
def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1132")
    print('TEXT', response_body.text)
    print('Status code', response_body.status_code)
    print('JSON', response_body.json())
    print('Headers :',response_body.headers)
    print(response_body.cookies)
    if response_body.status_code == 200:
        print("request successful")
    else :
        print("request unsuccessful")







if __name__ =="__main__":
    main()
