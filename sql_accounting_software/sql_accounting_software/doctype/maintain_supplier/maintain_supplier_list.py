from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time
from sql_accounting_software.sql_accounting_software.doctype.list_controller import ListController
# from autocount.autocount.doctype.autocount_settings import autocount_settings

DOCTYPE = "maintain supplier"
DOCTYPE_URL_NAME = "AP_Supplier"
ERP_PRIMARY_KEY = "code"
AUTOCOUNT_PRIMARY_KEY = "CODE"
URL_GET_ALL = f"{DOCTYPE_URL_NAME}/getAll"
URL_DETAIL = f"{DOCTYPE_URL_NAME}/getDetail"


def match_erp_with_api_json(data):
	# child_items = data["ChildItems"]
	new_child_list = []
	# if len(child_items) != 0:
	# 	for child in child_items:
	# 		x = {
	# 		"sales_ac": child["ACCOUNT"],
	# 		"description": child["DESCRIPTION"],
	# 		"amount": child["AMOUNT"],
	# 		"tax": child["TAX"],
	# 		"tax_rate": child["TAXRATE"],
	# 		"tax_inclusive": child["TAXINCLUSIVE"],
	# 		"tax_amt": child["TAXAMT"],
	# 		"sub_total": child["LOCALAMOUNT"]
	# 		}
	# 		new_child_list.append(x)

	output_data = {
    "code":  data.get("CODE"),
    "company":  data.get("COMPANYNAME"),
    "control_ac":  data.get("CONTROLACCOUNT"),
    "gst_no":  data.get("GSTNO"),
    "supp_category":  data.get("COMPANYCATEGORY"),
    # "branch_name":  data.get("TERMS"),
    # "address":  data.get("CANCELLED"),
    # "coordinate":  data.get("CURRENCYCODE"),
    # "attention":  data.get("DOCDATE"),
    # "phone":  data.get("DOCNOEX"),
    # "mobile":  new_child_list,
    # "fax":  data.get("DOCAMT"),
    # "email":  data.get("P_PAYMENTMETHOD"),
    "area":  data.get("AREA"),
    "agent":  data.get("AGENT"),
    "currency":  data.get("CURRENCYCODE"),
    "credit_terms":  data.get("CREDITTERM"),
    # "statement":  data.get("STATEMENTTYPE"),
    # "aging_on":  data.get("AGINGON"),
    # "price_tag":  data.get("PRICETAG")
	}
	return output_data

@frappe.whitelist()
def update():
	# controller = ListController(DOCTYPE, URL_GET_ALL, URL_DETAIL)
	controller = ListController(DOCTYPE, URL_GET_ALL)
	return controller.update_frappe(ERP_PRIMARY_KEY, AUTOCOUNT_PRIMARY_KEY, match_erp_with_api_json)