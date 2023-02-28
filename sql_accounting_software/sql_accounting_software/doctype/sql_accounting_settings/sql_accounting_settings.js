// Copyright (c) 2023, Richard and contributors
// For license information, please see license.txt


const defaultIPAddress = "127.0.0.1";
const defaultPort = "8000";

frappe.ui.form.on('sql accounting settings', {
	btn_test_connection: function(frm) {
		if (!frm.doc.ip_address) {
			frm.set_value("ip_address", defaultIPAddress);
		}

		if (!frm.doc.port) {
			frm.set_value("port", defaultPort);
		}

		frm.call({
			method: "sql_accounting_software.sql_accounting_software.doctype.sql_accounting_settings.sql_accounting_settings.test_connection",
			args:{
			    doc: frm.doc
			},
			freeze: true,
			callback:function(r){
				console.log(r.message);
				frappe.msgprint(r.message);
			},
		});
	},

	before_save: function(frm) {
		if (!frm.doc.ip_address) {
			frm.set_value("ip_address", defaultIPAddress);
		}

		if (!frm.doc.port) {
			frm.set_value("port", defaultPort);
		}
	}

});
