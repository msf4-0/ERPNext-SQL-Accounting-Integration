from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time
from sql_accounting_software.sql_accounting_software.doctype.list_controller import ListController
# from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "customer refund"
DOCTYPE_URL_NAME = "AR_CF"
ERP_PRIMARY_KEY = "cf_no"
AUTOCOUNT_PRIMARY_KEY = "DOCNO"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{DOCTYPE_URL_NAME}/getDetail"


def match_erp_with_api_json(data):
	child_items = data["ChildItems"]
	new_child_list = []
	if len(child_items) != 0:
		for child in child_items:
			x = {
			"doc_no": child["DOCNO"],
			"type": child["DOCTYPE"],
			"amount": child["DOCAMT"],
			"date": child["DOCDATE"],
			"unapplied_amt": child["OUTSTANDING"],
			"refund_amt": child["LOCALKOAMT"]
			}
			new_child_list.append(x)

	output_data = {
    "cf_no":  data.get("DOCNO"),
    "customer_code":  data.get("CODE"),
    "area":  data.get("AREA"),
    "agent":  data.get("AGENT"),
    "description":  data.get("DESCRIPTION"),
    "project":  data.get("PROJECT"),
    # "cancelled":  data.get("CANCELLED"),
    "currency":  data.get("CURRENCYCODE"),
    "date":  data.get("DOCDATE"),
    "customer_bank":  data.get("BANKACC"),
    "knock_off":  new_child_list,
    "total":  data.get("DOCAMT"),
    # "pay_to":  data.get("P_PAYMENTMETHOD"),
    # "payment_by":  data.get("LOCALDOCAMT"),
    "bank_charge":  data.get("BANKCHARGE"),
    "cheque_no":  data.get("CHEQUENUMBER"),
    "refund_amt":  data.get("LOCALDOCAMT"),
    "unapplied_amt":  data.get("UNAPPLIEDAMT")
	}
	return output_data

@frappe.whitelist()
def update():
	controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	# controller = ListController(DOCTYPE, URL_GET_ALL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)