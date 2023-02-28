# -*- coding: utf-8 -*-
# Copyright (c) 2023, Richard and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json
from sql_accounting_software.sql_accounting_software.doctype.form_controller import FormController
from sql_accounting_software.sql_accounting_software.doctype.utils import convert_date_string

DOCTYPE = "maintain stock group"
DOCTYPE_URL_NAME = "ST_GROUP"

controller = FormController(DOCTYPE_URL_NAME)

class maintainstockgroup(Document):
	def on_trash(self):
		doc_no = self.name
		controller.delete_on_autocount(doc_no)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)

	# Matches API key with ERPNext form key
	detail_list = []

	# if data.get("stock_received") is not None:
	# 	for item in data.get("stock_received"):
	# 		detail = {
	# 		"ITEMCODE" : item.get("item_code"),
	# 		"DESCRIPTION" : item.get("description"),
	# 		"LOCATION" : item.get("location"),
	# 		"UOM" : item.get("uom"),
	# 		"UNITCOST" : item.get("unit_cost"),
	# 		"PROJECT" : item.get("project"),
	# 		"AMOUNT" : item.get("sub_total"),
	# 		"QTY" : item.get("qty")
	# 		}
	# 		detail_list.append(detail)

	submitted_data = {
	"CODE":  data.get("code"),
    "DESCRIPTION":  data.get("description"),
    # "ISACTIVE":  data.get("DocNo"),
    # "COSTINGMETHOD":  data.get("costing_method"),
    "SALES":  data.get("sales_code"),
    "CASHSALES":  data.get("cash_sales_code"),
    "SALESRETURNED":  data.get("sreturn_code"),
    "PURCHASE":  data.get("purchase_code"),
    "CASHPURCHASE":  data.get("cash_purchase_code"),
    "PURCHASERETURNED":  data.get("preturn_code")
	}
	return submitted_data

@frappe.whitelist()
def add(doc):
	submitted_data = parse_doc(doc)
	return controller.add_to_autocount(submitted_data)

@frappe.whitelist()
def edit(doc):
	submitted_data = parse_doc(doc)
	return controller.edit_on_autocount(submitted_data)