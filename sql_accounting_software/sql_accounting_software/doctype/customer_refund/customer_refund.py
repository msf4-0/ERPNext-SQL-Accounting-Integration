# -*- coding: utf-8 -*-
# Copyright (c) 2023, Richard and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json
from sql_accounting_software.sql_accounting_software.doctype.form_controller import FormController
from sql_accounting_software.sql_accounting_software.doctype.utils import convert_date_string

DOCTYPE = "customer refund"
DOCTYPE_URL_NAME = "AR_CF"

controller = FormController(DOCTYPE_URL_NAME)

class customerrefund(Document):
	def on_trash(self):
		doc_no = self.name
		controller.delete_on_autocount(doc_no)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)

	# Matches API key with ERPNext form key
	detail_list = []

	if data.get("knock_off") is not None:
		for item in data.get("knock_off"):
			detail = {
			"DOCNO" : item.get("doc_no"),
			"DOCTYPE" : item.get("type"),
			"DOCAMT" : item.get("amount"),
			"DOCDATE" : item.get("date"),
			"OUTSTANDING" : item.get("unapplied_amt"),
			"LOCALKOAMT" : item.get("refund_amt")
			}
			detail_list.append(detail)

	submitted_data = {
	"DOCNO":  data.get("cf_no"),
    "CODE":  data.get("customer_code"),
    "AREA":  data.get("area"),
    "AGENT":  data.get("agent"),
    "DESCRIPTION":  data.get("description"),
    "PROJECT":  data.get("project"),
    # "cancelled":  data.get("CANCELLED"),
    "CURRENCYCODE":  data.get("currency"),
    "DOCDATE":  data.get("date"),
    "BANKACC":  data.get("customer_bank"),
	"detailList" : detail_list,
    "BANKCHARGE":  data.get("bank_charge"),
    "DOCAMT":  data.get("total"),
	"CHEQUENUMBER":  data.get("cheque_no"),
	"LOCALDOCAMT":  data.get("refund_amt"),
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