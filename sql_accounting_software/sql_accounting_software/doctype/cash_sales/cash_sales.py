# -*- coding: utf-8 -*-
# Copyright (c) 2023, Richard and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json
from sql_accounting_software.sql_accounting_software.doctype.form_controller import FormController
from sql_accounting_software.sql_accounting_software.doctype.utils import convert_date_string

DOCTYPE = "cash sales"
DOCTYPE_URL_NAME = "SL_CS"

controller = FormController(DOCTYPE_URL_NAME)

class cashsales(Document):
	def on_trash(self):
		doc_no = self.name
		controller.delete_on_autocount(doc_no)

@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)

	# Matches API key with ERPNext form key
	detail_list = []

	if data.get("sales_order") is not None:
		for item in data.get("sales_order"):
			detail = {
			"ITEMCODE" : item.get("sales_ac"),
			"DESCRIPTION" : item.get("description"),
			"QTY" : item.get("amount"),
			"UOM" : item.get("uom"),
			"UNITPRICE" : item.get("uprice"),
			"DISC" : item.get("disc"),
			"AMOUNT" : item.get("sub_total"),
			"TAX" : item.get("tax"),
			"TAXRATE" : item.get("tax_rate"),
			# "TAXINCLUSIVE" : item.get("tax_inclusive"),
			"TAXAMT" : item.get("tax_amt"),
			"AmountWithTax" : item.get("sub_total_tax")
			}
			detail_list.append(detail)

	submitted_data = {
	# "docNo" : data.get("doc_no"), 
	# "debtorCode" : data.get("debtor_code"), 
	# "date" : convert_date_string(data.get("date")), 
	# "shipInfo" : data.get("ship_info"), 
	# "paymentMode" : data.get("payment_mode")[0], 
	# "cashPayment" : data.get("cash_payment"), 
	# "detailList" : detail_list,

	"DOCNO":  data.get("cs_no"),
    "CODE":  data.get("customer"),
    "ADDRESS1":  data.get("address"),
    "AGENT":  data.get("agent"),
    "DESCRIPTION":  data.get("description"),
    "TERMS":  data.get("terms"),
    # "cancelled":  data.get("DocNo"),
    "DOCREF1":  data.get("ref_1"),
    "DOCDATE":  data.get("date"),
    "DOCNOEX":  data.get("ext_no"),
	"detailList" : detail_list,
    "LOCALDOCAMT":  data.get("total"),
    "P_PAYMENTMETHOD":  data.get("payment_into"),
    "P_CHEQUENUMBER":  data.get("chq_no"),
    "P_PAYMENTPROJECT":  data.get("payment_project"),
    "P_BANKCHARGE":  data.get("bank_charges"),
    "P_AMOUNT":  data.get("amount")
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