// Copyright (c) 2023, Richard and contributors
// For license information, please see license.txt

// frappe.ui.form.on('cash sales', {
// 	after_save: function(frm) {
// 		fetch('http://<base-url>/api/method/frappe.auth.get_logged_user', {
// 			headers: {
// 				'Authorization': 'Bearer access_token'
// 			}
// 		})
// 		.then(r => r.json())
// 		.then(r => {
// 			console.log(r);
// 		})
// 		frappe.msgprint("hello")
// 	}
// });


const addMethod = "sql_accounting_software.sql_accounting_software.doctype.cash_sales.cash_sales.add";
const editMethod = "sql_accounting_software.sql_accounting_software.doctype.cash_sales.cash_sales.edit";

// function isUndefinedOrEmpty(x) {
// 	return x === undefined || x === "";
// }

// function isInt(x) {
// 	return /^\d+$/.test(x);
// }

// function isCash(frm) {
// 	return frm.doc.payment_mode.startsWith("1");
// }

// function updateSubtotal(cdt, cdn) {
// 	var item = locals[cdt][cdn]; 
// 	if (!isUndefinedOrEmpty(item.quantity) && !isUndefinedOrEmpty(item.unit_price) 
// 		&& !isUndefinedOrEmpty(item.discount)) {
// 		var subtotal = (item.quantity * item.unit_price) - item.discount;
// 		frappe.model.set_value(cdt, cdn, "subtotal", subtotal);
// 	}
// }

// function updateGrandTotal(frm) {
// 	var total = 0;
// 	for (var i = 0; i < frm.doc.item_table.length; i++) {
// 		total += frm.doc.item_table[i].subtotal;
// 	}
// 	total = parseFloat(total).toFixed(2);
// 	//console.log(`Grand total: ${total}`);
// 	frm.set_value("total", total);
// }

// function updateChange(frm) {
// 	if (isCash(frm)) {
// 		var change = frm.doc.cash_payment - frm.doc.total;
// 		change = parseFloat(change).toFixed(2);
// 		change = change < 0 ? 0 : change;
// 		frm.set_value("change", change);
// 	}
// }


// function updateOutstanding(frm) {
// 	if (isCash(frm)) {
// 		var outstanding = frm.doc.total - frm.doc.cash_payment;
// 		outstanding = outstanding < 0 ? 0 : outstanding;
// 	} else {
// 		var outstanding = frm.doc.total;
// 	}
	
// 	outstanding = parseFloat(outstanding).toFixed(2);
// 	frm.set_value("outstanding", outstanding);
// }



frappe.ui.form.on('cash sales', {
	// refresh: function(frm) {
	// 	frm.set_df_property("cash_payment", "hidden", 0);
	// 	frm.set_df_property("change", "hidden", 0);
	// 	frm.set_df_property("btn_pay_total", "hidden", 0);

	// 	// Hide cash payment, change and pay total button if payment mode is not cash
	// 	if (!isCash(frm)) {
	// 		frm.set_df_property("cash_payment", "hidden", 1);
	// 		frm.set_df_property("change", "hidden", 1);
	// 		frm.set_df_property("btn_pay_total", "hidden", 1);
	// 	}

	// 	// In edit mode, if the previous payment mode is cash, cannot change.
	// 	if (!frm.is_new()) {
	// 		if (isCash(frm)) {
	// 			frm.set_df_property("payment_mode", "read_only", 1);
	// 		}
	// 	}
	// },

	// payment_mode: function(frm) {
	// 	frm.set_df_property("cash_payment", "hidden", 0);
	// 	frm.set_df_property("change", "hidden", 0);
	// 	frm.set_df_property("btn_pay_total", "hidden", 0);

	// 	// Hide cash payment, change and pay total button if payment mode is not cash
	// 	if (!isCash(frm)) {
	// 		frm.set_df_property("cash_payment", "hidden", 1);
	// 		frm.set_df_property("change", "hidden", 1);
	// 		frm.set_df_property("btn_pay_total", "hidden", 1);
	// 	}
	// 	updateOutstanding(frm);
	// },

	// total: function(frm) {
	// 	updateChange(frm);
	// 	updateOutstanding(frm);
	// },

	// cash_payment: function(frm) {
	// 	updateChange(frm);
	// 	updateOutstanding(frm);
	// },

	// btn_pay_total: function(frm) {
	// 	if (isCash(frm)) {
	// 		frm.set_value("cash_payment", frm.doc.total);
	// 	}
	// },	

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


// frappe.ui.form.on('Sales Child Table', {
// 	item_table_add: function(frm, cdt, cdn) {
// 		updateSubtotal(cdt, cdn);
// 	},

// 	item_table_remove: function(frm, cdt, cdn) {
// 		updateGrandTotal(frm);
// 	},

// 	item_code: function(frm, cdt, cdn) {
// 		// Trigger when item_code in child table has changed
// 		var item = locals[cdt][cdn]; 
// 		var item_code = item.item_code;

// 		if (item_code) {
// 			frappe.call({
// 				method: "frappe.client.get",
// 				args:{
// 				    doctype: "Stock Item",
// 					name: item_code
// 				},
// 				callback:function(r){
// 					var uom = r.message.uom;
// 					var unitPrice = r.message.unit_cost;

// 					frappe.model.set_value(cdt, cdn, "uom", uom);
// 					frappe.model.set_value(cdt, cdn, "quantity", 1);
// 					frappe.model.set_value(cdt, cdn, "unit_price", unitPrice);
// 					frappe.model.set_value(cdt, cdn, "discount", 0);

// 					updateSubtotal(cdt, cdn);
// 				},
// 			});
// 		} else {
// 			frappe.model.set_value(cdt, cdn, "uom", undefined);
// 			frappe.model.set_value(cdt, cdn, "quantity", 1);
// 			frappe.model.set_value(cdt, cdn, "unit_price", 0);
// 			frappe.model.set_value(cdt, cdn, "discount", 0);
// 			updateSubtotal(cdt, cdn);
// 		}


// 	},

// 	unit_price: function(frm, cdt, cdn) {
// 		var item = locals[cdt][cdn];

// 		if (isUndefinedOrEmpty(item.unit_price)) {
// 			frappe.model.set_value(cdt, cdn, "unit_price", 0);
// 		}

// 		if (item.unit_price < 0) {
// 			frappe.msgprint("Unit price cannot be negative value.");
// 			frappe.model.set_value(cdt, cdn, "unit_price", 0);
// 		}

// 		updateSubtotal(cdt, cdn);
		
// 	},

// 	quantity: function(frm, cdt, cdn) {
// 		var item = locals[cdt][cdn]; 
		
// 		if (isUndefinedOrEmpty(item.quantity)) {
// 			frappe.msgprint("Quantity cannot be zero or empty. Remove the row if not used.");
// 			frappe.model.set_value(cdt, cdn, "quantity", 1);
// 		}

// 		if (item.quantity < 0) {
// 			frappe.msgprint("Quantity cannot be negative value.");
// 			frappe.model.set_value(cdt, cdn, "quantity", 1);
// 		}

// 		updateSubtotal(cdt, cdn);
// 	},

// 	discount: function(frm, cdt, cdn) {
// 		var item = locals[cdt][cdn]; 

// 		if (isUndefinedOrEmpty(item.discount)) {
// 			frappe.model.set_value(cdt, cdn, "discount", 0);
// 		}

// 		if (item.discount < 0) {
// 			frappe.msgprint("Discount cannot be negative value.");
// 			frappe.model.set_value(cdt, cdn, "discount", 0);
// 		}

// 		updateSubtotal(cdt, cdn);
// 	},

// 	subtotal: function(frm, cdt, cdn) {
// 		var item = locals[cdt][cdn]; 

// 		if (item.subtotal < 0) {
// 			frappe.msgprint("Subtotal cannot be negative value. \
// 				Please adjust the discount."); 	// Means discount is too large
// 			frappe.model.set_value(cdt, cdn, "discount", 0);		// Reset discount to 0
// 		}

// 		updateGrandTotal(frm);
// 	},
	
// });