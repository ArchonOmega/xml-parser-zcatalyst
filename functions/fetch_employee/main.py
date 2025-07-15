import requests
import zcatalyst_sdk
import os
import sys
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')

def get_crm_access_token():
    """
    Fetches a new access token using the refresh token stored in .env.
    """
    client_id = os.getenv("ZOHO_CLIENT_ID")
    client_secret = os.getenv("ZOHO_CLIENT_SECRET")
    refresh_token = os.getenv("ZOHO_REFRESH_TOKEN")

    if not client_id or not client_secret or not refresh_token:
        raise ValueError("Missing required OAuth credentials in .env file")

    url = "https://accounts.zoho.com/oauth/v2/token"
    payload = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token
    }

    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to refresh access token: {response.text}")

def handler(request, context=None):
    """
    Fetches the most recently registered employee from Zoho CRM.
    """
    access_token = get_crm_access_token()
    crm_api_url = "https://www.zohoapis.com/crm/v2/Employees"

    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json"
    }

    params = {
        "sort_order": "desc",
        "sort_by": "Created_Time",
        "per_page": 1  # Get only the most recent employee
    }

    # Step 4: Make the API Request
    response = requests.get(crm_api_url, headers=headers, params=params)
    response.encoding = 'utf-8'
    
    #print("Zoho CRM API Response:", response.status_code, response.text.encode('utf-8', errors='ignore').decode())

    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            employee = data["data"][0]  # Get the latest employee
            name_english = employee.get("Name_English", "Unknown")
            dateofbirth = employee.get("Date_of_Birth", "Unknown")
            civilid = employee.get("Name", "Unknown")
            phonenumber = employee.get("Phone", "Unknown")
            #print("Employee Data:", str(employee).encode('utf-8', errors='ignore').decode())
            #employee_name = f"{employee.get('Name_English', '')}".strip()

            return {
                "status": "success",
                "employee": {
                    "id": employee.get("id"),
                    "name_english": name_english,
                    "email": employee.get("Email"),
                    "dateofbirth": dateofbirth,
                    "civilid": civilid,
                    "phonenumber": phonenumber
                },
                "message": f"The most recently added employee is {name_english}."
            }

    return {"status": "error", "message": "No employees found in CRM."}
    