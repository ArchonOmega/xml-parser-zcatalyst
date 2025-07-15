import requests
#import zcatalyst_sdk
import os
import sys
import json
import traceback
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')


def get_crm_access_token():
    """
    Fetches a new access token using the refresh token stored in .env.
    """
    client_id = "1000.XI2RW1K2V3M8QMGTUSPX4SWKKRBWBS"
    client_secret = "c2cd4a81ccfad15a8695422df60b4baa50654ef856"
    refresh_token = "1000.40b1bb6bd9698baca3966abd7a7e5e0c.b953631888bd6755855e73dfd74bcd65"

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
    Updates the Account_Status field in Zoho CRM from 'Open' to 'Blocked'.
    """
    #print("update_account_status function has started execution with request as follows: ")
    #print(request)
    #print(dir(request))
    #print("---------------------------------")
    #print(context)
    #print(dir(context))
    #print(context.get_argument('account_id'))

    try:
        # Parse request data
        #print(f"Request __dict__: {request.__dict__}")   # Print available attributes
        # Print full request details
        print(f"Received request to update employee: {request}")
        account_id = context.get_argument('account_id')  # ✅ Get Employee ID from request

        if not account_id:
            return {"status": "error", "message": "Account ID is required."}
            
        
        print(f"Extracted Account ID: {account_id}")
        access_token = get_crm_access_token()
        

        crm_update_url = f"https://www.zohoapis.com/crm/v2/Employees/{account_id}"
        headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "Content-Type": "application/json"
        }

    # ✅ Update the "Account_Status" field to "Blocked"
        update_data = {
            "data": [
                {
                    "Account_Status": "Blocked"
                }
            ],
            "trigger": ["workflow"]
        }
        
        
        
        print(f"CRM Update URL: {crm_update_url}")
        print(f"Payload: {json.dumps(update_data, indent=4)}")

        response = requests.put(crm_update_url, headers=headers, json=update_data)

        if response.status_code == 200:
            print(f"Account {account_id} successfully updated to 'Blocked'.")
            return {"status": "success", "message": f"Account {account_id} updated to 'Blocked'."}
        else:
            print(f"Failed to update account status: {response.text}")
            return {"status": "error", "message": response.text}
            
    except Exception as e:
        print("ERROR OCCURRED! Full Stack Trace Below:")
        traceback.print_exc()  # ✅ Print full error traceback
        return {"status": "error", "message": str(e)}