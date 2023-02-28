# -*- coding: utf-8 -*-
# Copyright (c) 2022, Richard and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json
from sql_accounting_software.sql_accounting_software.doctype.form_controller import FormController
from sql_accounting_software.sql_accounting_software.doctype.utils import convert_date_string

DOCTYPE = "maintain supplier"
DOCTYPE_URL_NAME = "AP_Supplier"

controller = FormController(DOCTYPE_URL_NAME)

class maintainsupplier(Document):
	def on_trash(self):
		doc_no = self.name
		controller.delete_on_autocount(doc_no)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)

	# Matches API key with ERPNext form key
	detail_list = []

	# if data.get("sales_order") is not None:
	# 	for item in data.get("sales_order"):
	# 		detail = {
	# 		"ACCOUNT" : item.get("sales_ac"),
	# 		"DESCRIPTION" : item.get("description"),
	# 		"AMOUNT" : item.get("amount"),
	# 		"TAX" : item.get("tax"),
	# 		"TAXRATE" : item.get("tax_rate"),
	# 		"TAXINCLUSIVE" : item.get("tax_inclusive"),
	# 		"TAXAMT" : item.get("tax_amt"),
	# 		"LOCALAMOUNT" : item.get("sub_total")
	# 		}
	# 		detail_list.append(detail)

	submitted_data = {
    "CODE":  data.get("code"),
    "COMPANYNAME":  data.get("company"),
    "CONTROLACCOUNT":  data.get("control_ac"),
    "GSTNO":  data.get("gst_no"),
    "COMPANYCATEGORY":  data.get("supp_category"),
    "AREA":  data.get("area"),
    "AGENT":  data.get("agent"),
    "CURRENCYCODE":  data.get("currency"),
    "CURRENCYCODE":  data.get("credit_terms")
	# "CREDITTERM" : detail_list,
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