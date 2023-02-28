from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time
from sql_accounting_software.sql_accounting_software.doctype.list_controller import ListController
# from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "sql quotation"
DOCTYPE_URL_NAME = "SL_QT"
ERP_PRIMARY_KEY = "quo_no"
AUTOCOUNT_PRIMARY_KEY = "DOCNO"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{DOCTYPE_URL_NAME}/getDetail"

def match_erp_with_api_json(data):
	child_items = data["ChildItems"]
	new_child_list = []
	if len(child_items) != 0:
		for child in child_items:
			x = {
			"sales_ac": child["ITEMCODE"],
			"description": child["DESCRIPTION"],
			"amount": child["QTY"],
			"uom": child["UOM"],
			"uprice": child["UNITPRICE"],
			"disc": child["DISC"],
			"sub_total": child["AMOUNT"],
			"tax": child["TAX"],
			"tax_rate": child["TAXRATE"],
			# "tax_inclusive": child["TAXINCLUSIVE"],
			"tax_amt": child["TAXAMT"],
			"sub_total_tax": child["AmountWithTax"]
			# "discount": transform_discount(child["Discount"])
			}
			new_child_list.append(x)

	output_data = {
    "quo_no":  data.get("DOCNO"),
    "customer":  data.get("CODE"),
    "address":  data.get("ADDRESS1"),
    "agent":  data.get("AGENT"),
    "description":  data.get("DESCRIPTION"),
    "terms":  data.get("TERMS"),
    # "cancelled":  data.get("DocNo"),
    "ref_1":  data.get("DOCREF1"),
    "date":  data.get("DOCDATE"),
    "ext_no":  data.get("DOCNOEX"),
    "sales_order":  new_child_list,
    "total":  data.get("LOCALDOCAMT")
	}
	return output_data

@frappe.whitelist()
def update():
	controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)