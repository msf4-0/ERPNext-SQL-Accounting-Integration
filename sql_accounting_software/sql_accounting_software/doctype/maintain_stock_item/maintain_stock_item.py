# -*- coding: utf-8 -*-
# Copyright (c) 2023, Richard and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json
from sql_accounting_software.sql_accounting_software.doctype.form_controller import FormController
from sql_accounting_software.sql_accounting_software.doctype.utils import convert_date_string

DOCTYPE = "maintain stock item"
DOCTYPE_URL_NAME = "ST_ITEM"

controller = FormController(DOCTYPE_URL_NAME)

class maintainstockitem(Document):
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
    # "active":  data.get("DocNo"),
    "DOCDATE":  data.get("serial_no"),
    "STOCKCONTROL":  data.get("stock_control"),
    "STOCKGROUP":  data.get("item_group"),
    "UOM":  data.get("base_uom"),
    "REFCOST":  data.get("ref_cost"),
    "REFPRICE":  data.get("ref_price"),
    "SHELF":  data.get("shelf"),
    "REORDERLEVEL":  data.get("reorder_level"),
    "REORDERQTY":  data.get("reorder_qty"),
    "LEADTIME":  data.get("lead_time"),
    "SLTAX":  data.get("output_tax"),
    "PHTAX":  data.get("input_tax"),
    "REMARK1":  data.get("remark_1"),
    "REMARK2":  data.get("remark_2"),
    "BARCODE":  data.get("barcode"),
    "TARIFF":  data.get("tariff"),
    "BALSQTY":  data.get("bal_qty")
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