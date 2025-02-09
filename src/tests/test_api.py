import json
import requests
from data import *
import pytest

import os

base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up one level
file_path = os.path.join(base_dir, "data", "credentials.json")

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Error: {file_path} not found.")

print("File found at:", file_path)

with open(file_path, "r") as file:
    credentials = json.load(file)

username = credentials["username"]
password = credentials["password"]

print(username,password)

# Define API endpoints
BASE_URL = "https://parabank.parasoft.com/parabank"
LOGIN_URL = f"{BASE_URL}/index.htm"

# Perform Login API Request
session = requests.Session()
payload = {"username": "omega2364@gmail.com", "password": "Password123"}

response = session.post(LOGIN_URL, data=payload)
@pytest.mark.order(-1)  # Runs this test last
def test_api():
    if "JSESSIONID" in response.cookies:
        jsession_id = response.cookies["JSESSIONID"]
        print(f"✅ Login successful! JSESSIONID: {jsession_id}")
        assert True
    else:
        assert False

@pytest.mark.order(-1)  # Runs this test last
def test_api():
    assert response.status_code == 200
