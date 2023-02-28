# -*- coding: utf-8 -*-
# Copyright (c) 2023, Richard and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json
from sql_accounting_software.sql_accounting_software.doctype.form_controller import FormController
from sql_accounting_software.sql_accounting_software.doctype.utils import convert_date_string

DOCTYPE = "supplier contra"
DOCTYPE_URL_NAME = "AP_ST"

controller = FormController(DOCTYPE_URL_NAME)

class suppliercontra(Document):
	def on_trash(self):
		doc_no = self.name
		controller.delete_on_autocount(doc_no)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)

	# Matches API key with ERPNext form key
	detail_list = []

	if data.get("knock_off_invoice_debit_notes") is not None:
		for item in data.get("knock_off_invoice_debit_notes"):
			detail = {
			"DOCNO" : item.get("doc_no"),
			"DOCTYPE" : item.get("type"),
			"DOCAMT" : item.get("amount"),
			"DOCDATE" : item.get("date"),
			"OUTSTANDING" : item.get("outstanding"),
			"LOCALKOAMT" : item.get("pay")
			}
			detail_list.append(detail)

	submitted_data = {
	"DOCNO":  data.get("ct_no"),
    "CODE":  data.get("customer_code"),
    "AREA":  data.get("area"),
    "AGENT":  data.get("agent"),
    "DESCRIPTION":  data.get("description"),
    "PROJECT":  data.get("project"),
    # "cancelled":  data.get("CANCELLED"),
    "CURRENCYCODE":  data.get("currency"),
    "DOCDATE":  data.get("date"),
    # "DOCNOEX":  data.get("ext_no"),
	"detailList" : detail_list,
    "LOCALDOCAMT":  data.get("local_amount"),
    "DOCAMT":  data.get("total"),
	"UNAPPLIEDAMT":  data.get("unapplied_amt")
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