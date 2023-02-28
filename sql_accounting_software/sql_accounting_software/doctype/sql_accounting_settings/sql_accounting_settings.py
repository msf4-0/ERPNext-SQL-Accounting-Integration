# -*- coding: utf-8 -*-
# Copyright (c) 2023, Richard and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


import requests
import json


class sqlaccountingsettings(Document):
	pass


@frappe.whitelist()
def parse_doc(doc):
	data = json.loads(doc)
	ip_address = data.get("ip_address")
	port = data.get("port")
	return f"http://{ip_address}:{port}"

@frappe.whitelist()
def test_connection(doc):
	ip_address = parse_doc(doc)
	url = f"{ip_address}/SL_CS/getAll"
	print(url)
	try:
		res = requests.get(url, timeout = 10)
		if res.status_code == 200:
			return "Connection success"
		# return f"HTTP Error: {res.status_code}"
	except Exception as ex:
		return str(ex)