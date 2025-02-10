import json
import requests
import os
import pytest

base_dir = os.path.dirname(os.path.dirname(__file__))  
file_path = os.path.join(base_dir, "data", "credentials.json")

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Error: {file_path} not found.")

with open(file_path, "r") as file:
    credentials = json.load(file)

USERNAME = credentials["username"]
PASSWORD = credentials["password"]

# API Endpoints
BASE_URL = "https://parabank.parasoft.com/parabank"
LOGIN_URL = f"{BASE_URL}/index.htm"

# Create a session for API calls
session = requests.Session()

@pytest.fixture(scope="session")
def get_session_id():
    """Logs in and returns a valid JSESSIONID for reuse."""
    payload = {"username": USERNAME, "password": PASSWORD}
    response = session.post(LOGIN_URL, data=payload)
    assert response.status_code == 200, f"Login failed: {response.text}"
    if "JSESSIONID" in response.cookies:
        jsession_id = response.cookies["JSESSIONID"]
        print(f"✅ Login successful! JSESSIONID: {jsession_id}")
        return jsession_id
    else:
        pytest.fail("JSESSIONID not found in cookies")

@pytest.mark.order(-1)  
def test_login(get_session_id):
    """Test if login was successful and JSESSIONID was obtained."""
    assert get_session_id is not None, "Session ID is missing"

@pytest.fixture
def get_accounts(get_session_id):
    """Fetch all account IDs using the stored session ID."""
    headers = {
        "Accept": "application/json",
        "Cookie": f"JSESSIONID={get_session_id}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = session.get(f"{BASE_URL}/services/bank/customers/12212/accounts", headers=headers)  
    assert response.status_code == 200, f"API call failed: {response.text}"
    accounts = response.json()
    assert isinstance(accounts, list), "Response is not a list"
    account_ids = [account["id"] for account in accounts]
    assert len(account_ids) > 0, "No accounts found"
    return account_ids

@pytest.mark.order(-1)  # Runs this test last
def test_account_ids(get_accounts):
    """Test if account IDs are fetched successfully."""
    assert all(isinstance(acc_id, int) for acc_id in get_accounts), "Some account IDs are not integers"
    print("✅ Account IDs:", get_accounts)

