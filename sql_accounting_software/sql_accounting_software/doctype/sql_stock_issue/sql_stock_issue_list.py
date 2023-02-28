from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time
from sql_accounting_software.sql_accounting_software.doctype.list_controller import ListController
# from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "sql stock issue"
DOCTYPE_URL_NAME = "ST_IS"
ERP_PRIMARY_KEY = "stk_issue_no"
AUTOCOUNT_PRIMARY_KEY = "DOCNO"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{DOCTYPE_URL_NAME}/getDetail"

def match_erp_with_api_json(data):
	child_items = data["ChildItems"]
	new_child_list = []
	if len(child_items) != 0:
		for child in child_items:
			x = {
			"item_code": child["ITEMCODE"],
			"description": child["DESCRIPTION"],
			"location": child["LOCATION"],
			"uom": child["UOM"],
			"unit_cost": child["UNITCOST"],
			"project": child["PROJECT"],
			# "sub_total": child["AMOUNT"],
			"qty": child["QTY"]
			}
			new_child_list.append(x)

	output_data = {
    "stk_issue_no":  data.get("DOCNO"),
    "description":  data.get("DESCRIPTION"),
    # "cancelled":  data.get("DocNo"),
    "date":  data.get("DOCDATE"),
    "stock_received":  new_child_list,
    "total":  data.get("DOCAMT"),
    "reason":  data.get("REASON"),
    "authorised_by":  data.get("AUTHBY"),
    "remark":  data.get("REMARK")
	}
	return output_data

@frappe.whitelist()
def update():
	controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)