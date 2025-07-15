import requests
import zcatalyst_sdk
import json

def get_email_access_token():
    """
    Fetches a new access token using the refresh token.
    """
    refresh_token = "1000.4dee3f9e4201e0c244db18e1e4a51505.655065ca313112f56940084fa4f80384"
    client_id = "1000.XI2RW1K2V3M8QMGTUSPX4SWKKRBWBS"
    client_secret = "c2cd4a81ccfad15a8695422df60b4baa50654ef856"

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


def send_email(match_name, civil_id, dob, mobile):
    """
    Sends an email notification when a match is found.
    """
    #catalyst_app = initialize()
    zoho_mail_url = "https://mail.zoho.com/api/accounts/8053536000000008002/messages"

    headers = {
        "Authorization": f"Zoho-oauthtoken {get_email_access_token()}",
        "Content-Type": "application/json"
    }

    email_data = {
    "fromAddress": "afouad@myrateb.com",
    "toAddress": "ahmedmedhat289@gmail.com",
    "ccAddress": "",
    "bccAddress": "",
    "subject": "Match Found in Sanctions List",
    "content": f"""
    A blacklisted user has registered on My Rateb with the following details:<br><br>
    <b>Civil ID</b>: {civil_id}<br>
    <b>Name</b>: {match_name}<br>
    <b>DOB</b>: {dob}<br>
    <b>Mobile number</b>: {mobile}<br><br>
    The account is now blocked to be reviewed by compliance.
    """,
    "askReceipt" : "yes"# ✅ Keep this to avoid sending as a draft
}


    response = requests.post(zoho_mail_url, headers=headers, json=email_data)

    print(f"Sending email to: {email_data['toAddress']}")
    print(f"Request Payload: {email_data}")
    print(f"Zoho API Response: {response.status_code}, {response.text}")

    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email: {response.text}")

def handler(request, context=None):
    """
    Compare the most recent Zoho CRM employee name with the UN sanctions alias list.
    """
    try:
        #catalyst_app = initialize()

        # Step 1: Fetch Most Recent Employee Name
        fetch_employee_url = "http://localhost:3000/server/fetch_employee/"
        employee_response = requests.post(fetch_employee_url)

        if employee_response.status_code != 200:
            return {"status": "error", "message": "Failed to fetch employee data"}

        employee_data = employee_response.json()
        if employee_data["status"] != "success":
            return {"status": "error", "message": "Employee data retrieval failed"}

        employee_name = employee_data["employee"]["name_english"]
        account_id = employee_data["employee"]["id"]
        date_of_birth = employee_data["employee"]["dateofbirth"]
        civil_id = employee_data["employee"]["civilid"]
        phone_number = employee_data["employee"]["phonenumber"]

        # Step 2: Fetch Alias Names from XML
        xml_parser_url = "http://localhost:3000/server/xml_parser/"
        alias_response = requests.post(xml_parser_url)

        if alias_response.status_code != 200:
            return {"status": "error", "message": "Failed to fetch alias data"}

        alias_data = alias_response.json()
        if alias_data["status"] != "success":
            return {"status": "error", "message": "Alias data retrieval failed"}

        alias_names = [name.lower() for individual in alias_data["individuals"] for name in individual["alias_names"]]

        # Step 3: Compare Employee Name with Alias List
        match_found = employee_name.lower() in alias_names
        
        if match_found:
            send_email(employee_name, civil_id, date_of_birth, phone_number)
            if account_id:
                update_status_url = "http://localhost:3000/server/update_account_status/"
                update_status_response = requests.post(update_status_url, json={"account_id": account_id})
                print(f"Sending account update request: {update_status_url} with payload {json.dumps({'account_id': account_id})}")

                if update_status_response.status_code != 200:
                    print(f"Update Status API Response: {update_status_response.status_code}, {update_status_response.text}")
                    return {"status": "error", "message": f"Failed to update employee status: {update_status_response.text}"}
            else:
                print("⚠ No Account ID found for this employee. Skipping account status update.")



        return {
            "status": "success",
            "employee_name": employee_name,
            "match_found": match_found,
            "message": "Match found in alias list, Account staus updated and email sent!" if match_found else "No match found."
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
