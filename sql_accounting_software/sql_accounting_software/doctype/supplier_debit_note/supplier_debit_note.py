# -*- coding: utf-8 -*-
# Copyright (c) 2023, Richard and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json
from sql_accounting_software.sql_accounting_software.doctype.form_controller import FormController
from sql_accounting_software.sql_accounting_software.doctype.utils import convert_date_string

DOCTYPE = "supplier debit note"
DOCTYPE_URL_NAME = "AP_SD"

controller = FormController(DOCTYPE_URL_NAME)

class supplierdebitnote(Document):
	def on_trash(self):
		doc_no = self.name
		controller.delete_on_autocount(doc_no)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)

	# Matches API key with ERPNext form key
	detail_list = []

	# if data.get("document_detail_grid") is not None:
	# 	for item in data.get("document_detail_grid"):
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
	"DOCNO":  data.get("inv_no"),
    "CODE":  data.get("supplier_code"),
    "AREA":  data.get("area"),
    "AGENT":  data.get("agent"),
    "DESCRIPTION":  data.get("dn_description"),
    "TERMS":  data.get("terms"),
    # "cancelled":  data.get("CANCELLED"),
    "CURRENCYCODE":  data.get("currency"),
    "DOCDATE":  data.get("date"),
    "DOCNOEX":  data.get("ext_no"),
	"detailList" : detail_list,
    # "LOCALDOCAMT":  data.get("local_net_total"),
    "DOCAMT":  data.get("total"),
	"OUTSTANDING":  data.get("outstanding")
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