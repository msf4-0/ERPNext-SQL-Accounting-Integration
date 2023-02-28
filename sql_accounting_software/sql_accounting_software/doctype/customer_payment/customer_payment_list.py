from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time
from sql_accounting_software.sql_accounting_software.doctype.list_controller import ListController
# from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "customer payment"
DOCTYPE_URL_NAME = "AR_PM"
ERP_PRIMARY_KEY = "or_no"
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
			"outstanding": child["OUTSTANDING"],
			"pay": child["LOCALKOAMT"]
			}
			new_child_list.append(x)

	output_data = {
    "or_no":  data.get("DOCNO"),
    "customer_code":  data.get("CODE"),
    "area":  data.get("AREA"),
    "agent":  data.get("AGENT"),
    "description":  data.get("DESCRIPTION"),
    "project":  data.get("PROJECT"),
    # "cancelled":  data.get("CANCELLED"),
    # "non_refundable":  data.get("CANCELLED"),
    "currency":  data.get("CURRENCYCODE"),
    "date":  data.get("DOCDATE"),
    # "from_deposit":  data.get("BANKACC"),
    "knock_off":  new_child_list,
    "total":  data.get("DOCAMT"),
    # "paid_by":  data.get("P_PAYMENTMETHOD"),
    # "received_in":  data.get("LOCALDOCAMT"),
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