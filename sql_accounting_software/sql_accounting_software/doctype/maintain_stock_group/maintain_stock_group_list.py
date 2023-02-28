from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time
from sql_accounting_software.sql_accounting_software.doctype.list_controller import ListController
# from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "maintain stock group"
DOCTYPE_URL_NAME = "ST_GROUP"
ERP_PRIMARY_KEY = "code"
AUTOCOUNT_PRIMARY_KEY = "CODE"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{DOCTYPE_URL_NAME}/getDetail"

def match_erp_with_api_json(data):
	# child_items = data["ChildItems"]
	# new_child_list = []
	# if len(child_items) != 0:
	# 	for child in child_items:
	# 		x = {
	# 		"item_code": child["ITEMCODE"],
	# 		"description": child["DESCRIPTION"],
	# 		"location": child["LOCATION"],
	# 		"uom": child["UOM"],
	# 		"unit_cost": child["UNITCOST"],
	# 		"project": child["PROJECT"],
	# 		"sub_total": child["AMOUNT"],
	# 		"qty": child["QTY"]
	# 		}
	# 		new_child_list.append(x)

	output_data = {
    "code":  data.get("CODE"),
    "description":  data.get("DESCRIPTION"),
    # "active":  data.get("ISACTIVE"),
    # "costing_method":  data.get("COSTINGMETHOD"),
    "sales_code":  data.get("CASHSALES"),
    "cash_sales_code":  data.get("SALESRETURNED"),
    "sreturn_code":  data.get("SALES"),
    # "balance_sheet_stock":  data.get("REMARK"),
    "purchase_code":  data.get("PURCHASE"),
    "cash_purchase_code":  data.get("CASHPURCHASE"),
    "preturn_code":  data.get("PURCHASERETURNED")
	}
	return output_data

@frappe.whitelist()
def update():
	# controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	controller = ListController(DOCTYPE, URL_GET_ALL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)