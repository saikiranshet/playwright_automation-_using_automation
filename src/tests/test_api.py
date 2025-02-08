import requests

url = "https://parabank.parasoft.com/parabank/services_proxy/bank/accounts/21891/transactions/onDate/02-08-2025?timeout=30000"
url2 = "https://parabank.parasoft.com/parabank/services_proxy/bank/accounts/21891/transactions/fromDate/02-08-2025/toDate/02-08-2025?timeout=30000"
url3 = "https://parabank.parasoft.com/parabank/services_proxy/bank/accounts/21780/transactions/amount/1000?timeout=30000"

headers = {
  'Cookie': 'JSESSIONID=27E795F5922CD85D55DB5C5363665259',
  'Referer': 'https://parabank.parasoft.com/parabank/findtrans.htm'
}

def test_status_code_ondate():
    response = requests.request("GET", url, headers=headers)
    assert response.status_code==200
    
def test_status_code_fromto():
    response = requests.request("GET", url2, headers=headers)
    assert response.status_code==200

def test_status_code_Amount():
    response = requests.request("GET", url3, headers=headers)
    assert response.status_code==200




