# -*- coding: utf-8 -*-
# Copyright (c) 2023, Richard and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json
from sql_accounting_software.sql_accounting_software.doctype.form_controller import FormController
from sql_accounting_software.sql_accounting_software.doctype.utils import convert_date_string

DOCTYPE = "stock received"
DOCTYPE_URL_NAME = "ST_RC"

controller = FormController(DOCTYPE_URL_NAME)

class stockreceived(Document):
	def on_trash(self):
		doc_no = self.name
		controller.delete_on_autocount(doc_no)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)

	# Matches API key with ERPNext form key
	detail_list = []

	if data.get("stock_received") is not None:
		for item in data.get("stock_received"):
			detail = {
			"ITEMCODE" : item.get("item_code"),
			"DESCRIPTION" : item.get("description"),
			"LOCATION" : item.get("location"),
			"UOM" : item.get("uom"),
			"UNITCOST" : item.get("unit_cost"),
			"PROJECT" : item.get("project"),
			"AMOUNT" : item.get("sub_total"),
			"QTY" : item.get("qty")
			}
			detail_list.append(detail)

	submitted_data = {
	"DOCNO":  data.get("stk_rec_no"),
    "DESCRIPTION":  data.get("description"),
    # "cancelled":  data.get("DocNo"),
    "DOCDATE":  data.get("date"),
	"stock_received" : detail_list,
    "DOCAMT":  data.get("total"),
	"REASON":  data.get("reason"),
    "AUTHBY":  data.get("authorised_by"),
    "REMARK":  data.get("remark")
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