# Copyright (c) 2025, SSDolui and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from myalgo_app.myalgo_app_custom.demat_api.angel_one import get_api, get_totp, get_holdings

def set_api_key(doc):
	doc.api_key= get_api()

class DematAccount(Document):
	def before_save(self):
		holding= get_holdings()
		print(holding)
		print("--------------------------------")
		set_api_key(self)
