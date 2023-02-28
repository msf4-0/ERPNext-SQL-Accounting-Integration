## Update the entire database ##

import time
import frappe

import datetime
import pytz
import os

import requests
import json

from sql_accounting_software.sql_accounting_software.doctype import url_config

from sql_accounting_software.sql_accounting_software.doctype.customer_invoice import customer_invoice_list
from sql_accounting_software.sql_accounting_software.doctype.maintain_customer import maintain_customer_list
from sql_accounting_software.sql_accounting_software.doctype.customer_contra import customer_contra_list
from sql_accounting_software.sql_accounting_software.doctype.customer_refund import customer_refund_list
from sql_accounting_software.sql_accounting_software.doctype.customer_payment import customer_payment_list 
from sql_accounting_software.sql_accounting_software.doctype.customer_debit_note import customer_debit_note_list
from sql_accounting_software.sql_accounting_software.doctype.customer_credit_note import customer_credit_note_list

from sql_accounting_software.sql_accounting_software.doctype.supplier_invoice import supplier_invoice_list
from sql_accounting_software.sql_accounting_software.doctype.maintain_supplier import maintain_supplier_list
from sql_accounting_software.sql_accounting_software.doctype.supplier_contra import supplier_contra_list
from sql_accounting_software.sql_accounting_software.doctype.supplier_refund import supplier_refund_list
from sql_accounting_software.sql_accounting_software.doctype.supplier_payment import supplier_payment_list
from sql_accounting_software.sql_accounting_software.doctype.supplier_debit_note import supplier_debit_note_list
from sql_accounting_software.sql_accounting_software.doctype.supplier_credit_note import supplier_credit_note_list

from sql_accounting_software.sql_accounting_software.doctype.sql_sales_order import sql_sales_order_list
from sql_accounting_software.sql_accounting_software.doctype.sql_quotation import sql_quotation_list
from sql_accounting_software.sql_accounting_software.doctype.sql_delivery_order import sql_delivery_order_list
from sql_accounting_software.sql_accounting_software.doctype.invoice import invoice_list
from sql_accounting_software.sql_accounting_software.doctype.cash_sales import cash_sales_list
from sql_accounting_software.sql_accounting_software.doctype.sql_credit_note import sql_credit_note_list
from sql_accounting_software.sql_accounting_software.doctype.sql_debit_note import sql_debit_note_list

from sql_accounting_software.sql_accounting_software.doctype.sql_purchase_order import sql_purchase_order_list
from sql_accounting_software.sql_accounting_software.doctype.purchase_request import purchase_request_list
from sql_accounting_software.sql_accounting_software.doctype.goods_received import goods_received_list
from sql_accounting_software.sql_accounting_software.doctype.sql_purchase_invoice import sql_purchase_invoice_list
from sql_accounting_software.sql_accounting_software.doctype.cash_purchase import cash_purchase_list
from sql_accounting_software.sql_accounting_software.doctype.purchase_debit_note import purchase_debit_note_list
from sql_accounting_software.sql_accounting_software.doctype.purchase_returned import purchase_returned_list

from sql_accounting_software.sql_accounting_software.doctype.stock_received import stock_received_list
from sql_accounting_software.sql_accounting_software.doctype.maintain_stock_group import maintain_stock_group_list
from sql_accounting_software.sql_accounting_software.doctype.maintain_stock_item import maintain_stock_item_list
from sql_accounting_software.sql_accounting_software.doctype.sql_stock_issue import sql_stock_issue_list
from sql_accounting_software.sql_accounting_software.doctype.sql_stock_adjustment import sql_stock_adjustment_list

def filter_msg(results):
	# Only showing msg when there are changes (deleted, added, edited)
	# Calculate total time
	msg = ""
	time = 0
	for result in results:
		time += result["time"]
		if any([result["deleted"], result["added"], result["edited"]]):
			msg += f"\n{result}"
	if msg == "":
		msg += f"\nAll skipped"
	msg += f"\nTotal time: {time} seconds"
	return msg


@frappe.whitelist()
def update_all_tables():
	a= customer_invoice_list.update()
	b= maintain_customer_list.update()
	c= customer_contra_list.update()
	d= customer_refund_list.update()
	e= customer_payment_list.update()
	f= customer_debit_note_list.update()
	g= customer_credit_note_list.update()

	h= supplier_invoice_list.update()
	i= maintain_supplier_list.update()
	j= supplier_contra_list.update()
	k= supplier_refund_list.update()
	l= supplier_payment_list.update()
	m= supplier_debit_note_list.update()
	n= supplier_credit_note_list.update()

	o= sql_sales_order_list.update()
	p= sql_quotation_list.update()
	q= sql_delivery_order_list.update()
	r= invoice_list.update()
	s= cash_sales_list.update()
	t= sql_credit_note_list.update()
	u= sql_debit_note_list.update()

	v= sql_purchase_order_list.update()
	w= purchase_request_list.update()
	x= goods_received_list.update()
	y= sql_purchase_invoice_list.update()
	z= cash_purchase_list.update()
	aa= purchase_debit_note_list.update()
	ab= purchase_returned_list.update()
	
	ac= stock_received_list.update()
	ad= maintain_stock_group_list.update()
	ae= maintain_stock_item_list.update()
	af= sql_stock_issue_list.update()
	ag= sql_stock_adjustment_list.update()

	return filter_msg([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, ac, ad, ae, af, ag])
