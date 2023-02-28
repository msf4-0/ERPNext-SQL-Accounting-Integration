from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time
from sql_accounting_software.sql_accounting_software.doctype.list_controller import ListController
# from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "supplier debit note"
DOCTYPE_URL_NAME = "AP_SD"
ERP_PRIMARY_KEY = "dn_no"
AUTOCOUNT_PRIMARY_KEY = "DOCNO"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{DOCTYPE_URL_NAME}/getDetail"


def match_erp_with_api_json(data):
	# child_items = data["ChildItems"]
	# new_child_list = []
	# if len(child_items) != 0:
	# 	for child in child_items:
	# 		x = {
	# 		"sales_ac": child["ACCOUNT"],
	# 		"description": child["DESCRIPTION"],
	# 		"amount": child["AMOUNT"],
	# 		"tax": child["TAX"],
	# 		"tax_rate": child["TAXRATE"],
	# 		"tax_inclusive": child["TAXINCLUSIVE"],
	# 		"tax_amt": child["TAXAMT"],
	# 		"sub_total": child["LOCALAMOUNT"]
	# 		}
	# 		new_child_list.append(x)

	output_data = {
    "dn_no":  data.get("DOCNO"),
    "supplier_code":  data.get("CODE"),
    "area":  data.get("AREA"),
    "agent":  data.get("AGENT"),
    "dn_description":  data.get("DESCRIPTION"),
    "terms":  data.get("TERMS"),
    # "cancelled":  data.get("CANCELLED"),
    "currency":  data.get("CURRENCYCODE"),
    "date":  data.get("DOCDATE"),
    "ext_no":  data.get("DOCNOEX"),
    # "document_detail_grid":  new_child_list,
    "total":  data.get("DOCAMT"),
    # "bill_from":  data.get("P_PAYMENTMETHOD"),
    # "local_net_total":  data.get("LOCALDOCAMT"),
    "outstanding":  data.get("OUTSTANDING")
    # "bank_charges":  data.get("P_BANKCHARGE"),
    # "amount":  data.get("P_AMOUNT"),
	}
	return output_data

@frappe.whitelist()
def update():
	# controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	controller = ListController(DOCTYPE, URL_GET_ALL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)