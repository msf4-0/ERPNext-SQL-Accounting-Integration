// Copyright (c) 2023, Richard and contributors
// For license information, please see license.txt

const addMethod = "sql_accounting_software.sql_accounting_software.doctype.maintain_stock_group.maintain_stock_group.add";
const editMethod = "sql_accounting_software.sql_accounting_software.doctype.maintain_stock_group.maintain_stock_group.edit";


frappe.ui.form.on('maintain stock group', {
	// refresh: function(frm) {

	// }
	before_save: function(frm) {
		if (frm.is_new()) {
			console.log("new form");
		 	frm.call({
				method: addMethod,
				args:{
				    doc: frm.doc
				},
				freeze: true,
				callback: function(r) {
					if (!r.exc) {
						console.log("Added successfully");
						
					} 
					console.log(r.message);
				},
				error: function(r) {
					console.log("Added failed");
					frappe.validated = false;
				}
			})
		} else {
			console.log("edit form");
			frm.call({
				method: editMethod,
				args:{
				    doc: frm.doc
				},
				freeze: true,
				callback: function(r) {
					if (!r.exc) {
						console.log("Edited successfully");
						
					} 
					console.log(r.message);
				},
				error: function(r) {
					console.log("Edited failed");
					frappe.validated = false;
				}
			}) 
			
		}
	},

});
