
import pyotp
from SmartApi.smartConnect import SmartConnect
import frappe
import logging



angel_one_keys= {
    "api_key": "d0scKIWZ",
    "totp_key": "ELIKSOBSAGFTYN726GV3TM5U7M",
    "client_id": "J58605296",
    "password": "4916"
}

@frappe.whitelist()
def get_api():
    api_key = angel_one_keys["api_key"]
    return api_key

@frappe.whitelist()
def get_totp():
    totp_key = angel_one_keys["totp_key"]
    totp = pyotp.TOTP(totp_key).now()
    return totp



@frappe.whitelist()
def get_holdings():
    """
    Fetch current holdings from Angel One
    """
    try:
        api_key = angel_one_keys["api_key"]
        totp_secret = angel_one_keys["totp_key"]
        client_id = angel_one_keys["client_id"]
        password = angel_one_keys["password"]

        # Generate TOTP
        token = pyotp.TOTP(totp_secret).now()

        # Initialize SmartConnect
        obj = SmartConnect(api_key=api_key)
        session = obj.generateSession(client_id, password, token)
        # You can store refreshToken if needed: session['data']['refreshToken']

        # Fetch holdings
        holdings = obj.holding()  # correct method is `holding()` not `holdings()`
        return holdings

    except Exception as e:
        logging.error(f"Failed to fetch holdings: {e}")
        frappe.throw(f"Failed to fetch holdings: {e}")