from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

# DEFAULT_IP_ADDRESS = "host.docker.internal"
DEFAULT_IP_ADDRESS = "127.0.0.1"
DEFAULT_PORT = "8000"

@frappe.whitelist()
def get_socket_address():
	data = frappe.db.get("sql accounting settings")

	if not data:
		return f"http://{DEFAULT_IP_ADDRESS}:{DEFAULT_PORT}"

	ip_address = data.get("ip_address")
	port = data.get("port")

	if not ip_address:
		ip_address = DEFAULT_IP_ADDRESS
		frappe.db.set_value("Autocount Settings", "Autocount Settings", "ip_address", DEFAULT_IP_ADDRESS)
		frappe.db.commit()
		
	if not port:
		port = DEFAULT_PORT
		frappe.db.set_value("Autocount Settings", "Autocount Settings", "port", DEFAULT_PORT)
		frappe.db.commit()

	return f"http://{ip_address}:{port}"


	
