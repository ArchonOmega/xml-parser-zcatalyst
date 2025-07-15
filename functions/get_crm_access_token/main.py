import requests
import os
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

def get_crm_access_token():
    """
    Fetches a new access token using the refresh token stored in .env.
    """
    client_id = os.getenv("1000.XI2RW1K2V3M8QMGTUSPX4SWKKRBWBS")
    client_secret = os.getenv("c2cd4a81ccfad15a8695422df60b4baa50654ef856")
    refresh_token = os.getenv("1000.4141c1a931b8e9618e8fe3ad09091b69.7ea446a357bc9c3c1e79c496d30407c7")

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