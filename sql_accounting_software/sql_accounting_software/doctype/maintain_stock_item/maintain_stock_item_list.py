from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time
from sql_accounting_software.sql_accounting_software.doctype.list_controller import ListController
# from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "maintain stock item"
DOCTYPE_URL_NAME = "ST_ITEM"
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
    # "active":  data.get("DocNo"),
    "serial_no":  data.get("DOCDATE"),
    "stock_control":  data.get("STOCKCONTROL"),
    "item_group":  data.get("STOCKGROUP"),
    "base_uom":  data.get("UOM"),
    "ref_cost":  data.get("REFCOST"),
    "ref_price":  data.get("REFPRICE"),
    "shelf":  data.get("SHELF"),
    "reorder_level":  data.get("REORDERLEVEL"),
    "reorder_qty":  data.get("REORDERQTY"),
    "lead_time":  data.get("LEADTIME"),
    "output_tax":  data.get("SLTAX"),
    "input_tax":  data.get("PHTAX"),
    "remark_1":  data.get("REMARK1"),
    "remark_2":  data.get("REMARK2"),
    "barcode":  data.get("BARCODE"),
    "tariff":  data.get("TARIFF"),
    "bal_qty":  data.get("BALSQTY")
	}
	return output_data

@frappe.whitelist()
def update():
	# controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	controller = ListController(DOCTYPE, URL_GET_ALL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)