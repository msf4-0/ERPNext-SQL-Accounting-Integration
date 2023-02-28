
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import requests
import json
import time

from sql_accounting_software.sql_accounting_software.doctype.utils import datetime_to_t_format
# from sql_accounting_software.sql_accounting_software.doctype.autocount_settings import autocount_settings

from sql_accounting_software.sql_accounting_software.doctype import url_config

class ListController:
	def __init__(self, doctype, url_get_all, url_detail = None):
		self.doctype = doctype
		self.socket_address = url_config.get_socket_address()		# update.py initializes everytime, no need to update

		self.url_get_all = f"{self.socket_address}/{url_get_all}"
		self.url_detail = url_detail
		if url_detail is not None:
			self.url_detail = f"{self.socket_address}/{url_detail}"

		self.has_child_table = self.has_child_table()

	def has_child_table(self):
		if not self.url_detail:
			return False
		return True

	def connect(self):
		frappe.connect()

	def commit(self):
		frappe.db.commit()

	def get_all(self):
		if self.has_child_table:
			return [frappe.get_doc(self.doctype, item.name).as_dict() for item in frappe.get_all(self.doctype)]
		return frappe.get_all(self.doctype, fields = ["*"])

	def fetch_data_from_autocount(self, autocount_primary_key = None):
		parents = json.loads(requests.get(self.url_get_all).text)
		if self.has_child_table:
			if len(parents) != 0:
				for parent in parents:
					child = json.loads(requests.get(f"{self.url_detail}/{parent[autocount_primary_key]}").text)
					parent["ChildItems"] = child
		return parents

	def add(self, data):
		doc = frappe.get_doc( **{"doctype": self.doctype}, **data )		# merge two dicts
		doc.insert()

	def edit(self, title, data, erp_primary_key):
		doc = frappe.get_doc(self.doctype, data[erp_primary_key])
		for k, v in data.items():
			doc.set(k, v)
		doc.save()

	def delete(self, title):
		frappe.delete_doc(self.doctype, title)

	def delete_all(self, commit = False):
		title_list = [doc["name"] for doc in frappe.get_all(self.doctype)]
		for title in title_list:
			frappe.delete_doc(self.doctype, title)
		if commit is True:
			frappe.db.commit()

	def match_dicts(self, erp_dict, autocount_dict):
		"""
		Select {key,value} from erp_dict where key is in autocount_dict,
		to compare with autocount_dict to determine whether edit or skip.
		"""
		result = {k:v for k,v in erp_dict.items() if k in autocount_dict.keys()}
		# if "date" in result.keys():
		# 	result["date"] = datetime_to_t_format(result["date"])
		if self.has_child_table:
			child_table_name = [k for k,v in result.items() if isinstance(v, list)][0]
			child_list = result[child_table_name]
			if len(child_list) > 0:
				new_child_list = []
				child_keys = autocount_dict[child_table_name][0].keys()
				for child in child_list:
					matched_child = {k:v for k,v in child.items() if k in child_keys}
					new_child_list.append(matched_child)
				result[child_table_name] = new_child_list
		return result


	# def update_stock_item(self):
	# 	# import sql_accounting_software.sql_accounting_software.doctype.stock_item.stock_item_list as st
	# 	# return st.update()

	# 	def create_data_map(data):
	# 		output_data = {
	# 		"item_code" : data["ItemCode"], 
	# 		"description" : data["Description"], 
	# 		"uom" : data["BaseUOM"]
	# 		}
	# 		return output_data

	# 	controller = ListController("Stock Item", "http://host.docker.internal:1234/StockItem/getAll")
	# 	return controller.update_frappe("item_code", "ItemCode", create_data_map)
						

	@frappe.whitelist()
	def update_frappe(self, erp_primary_key, autocount_primary_key, create_data_map):
		start_time = time.time()
		erp = self.get_all()
		autocount = self.fetch_data_from_autocount(autocount_primary_key)
		
		""" 
		If erp exists but autocount not exists, means data being deleted in autocount.
		The data will be deleted in erp.
		"""
		erp_item_code = [x[erp_primary_key] for x in erp]
		autocount_item_code = [x[autocount_primary_key] for x in autocount]

		deleted_list = list(set(erp_item_code) - set(autocount_item_code))
		if len(deleted_list) > 0:
			for each in deleted_list:
				# print(f"Deleting: {each}")
				self.delete(each)
			print(f"Deleted {len(deleted_list)} data.")

		"""
		If autocount exists but erp not exists, means data is being added from autocount.
		The data will be added to erp.
		"""
		added_list = list(set(autocount_item_code) - set(erp_item_code))
		if len(added_list) > 0:
			for each in added_list:
				raw_autocount_data = [x for x in autocount if x[autocount_primary_key] == each][0]
				processed_autocount_data = create_data_map(raw_autocount_data)
				# print(f"Adding: {each}")
				self.add(processed_autocount_data)
			print(f"Added {len(added_list)} data.")

		"""
		If both autocount and erp exist, have to check if data has been edited from autocount.
		If data is different from autocount: edit, else skip.
		"""
		edited_list = list(set(erp_item_code).intersection(autocount_item_code))

		editted = 0
		skipped = 0

		if len(edited_list) > 0:
			for each in edited_list:
				raw_autocount_data = [x for x in autocount if x[autocount_primary_key] == each][0]	# locate autocount dict with same primary key

				processed_autocount_data = create_data_map(raw_autocount_data)	# filter autocount data to select only key,value used in erpnext

				raw_erp_data = [x for x in erp if x[erp_primary_key] == each][0]
				processed_erp_data = self.match_dicts(raw_erp_data, processed_autocount_data)

				if processed_erp_data == processed_autocount_data:
					skipped += 1
					print("Skipped:")
					print(f"ERP: {processed_erp_data}")
					print(f"Autocount: {processed_autocount_data}")
					print("\n")
				else:
					self.edit(each, processed_autocount_data, erp_primary_key)
					editted += 1
					print("Edited:")
					print(f"ERP: {processed_erp_data}")
					print(f"Autocount: {processed_autocount_data}")
					print("\n")

			print(f"Edited {editted} data.")
			print(f"Skipped {skipped} data.")

		self.commit()
		end_time = time.time()
		duration = end_time - start_time
		msg = {"doctype": self.doctype, "deleted": len(deleted_list), "added": len(added_list),
		"edited": editted, "skipped": skipped, "time": duration}
		return msg
