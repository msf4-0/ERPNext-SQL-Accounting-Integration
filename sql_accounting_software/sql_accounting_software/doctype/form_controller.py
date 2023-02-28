
from __future__ import unicode_literals
import frappe

import requests
import time

# from sql_accounting_software.sql_accounting_software.doctype.autocount_settings import autocount_settings
from sql_accounting_software.sql_accounting_software.doctype import url_config

class FormController:
	def __init__(self, doctype_url_name):
		self.socker_address = url_config.get_socket_address()
		self.doctype_url_name = doctype_url_name
		self.url_add = f"{self.socker_address}/{self.doctype_url_name}/add"
		self.url_edit = f"{self.socker_address}/{self.doctype_url_name}/edit"
		self.url_delete = f"{self.socker_address}/{self.doctype_url_name}/delete"

	def update_socket_address(self):
		self.socker_address = url_config.get_socket_address()

	def add_to_autocount(self, data):
		start_time = time.time()
		self.update_socket_address()
		res = requests.post(self.url_add, json = data)
		end_time = time.time()
		if res.status_code == 200:
			return f"{res.text}\n(Done in {end_time - start_time} seconds)\n"
		frappe.throw(res.text, title = "Server Exception")


	def edit_on_autocount(self, data):
		start_time = time.time()
		self.update_socket_address()
		res = requests.put(self.url_edit, json = data)
		end_time = time.time()
		if res.status_code == 200:
			return f"{res.text}\n(Done in {end_time - start_time} seconds)\n"
		frappe.throw(res.text, title = "Server Exception")

	def delete_on_autocount(self, key):
		self.update_socket_address()
		res = requests.delete(f"{self.url_delete}/{key}")
		if res.status_code == 200:
			frappe.msgprint(res.text)
			return res.text
		# Comment: Will delete ERPNext even if HTTP Error
		# frappe.throw(res.text, title = "Server Exception")	
