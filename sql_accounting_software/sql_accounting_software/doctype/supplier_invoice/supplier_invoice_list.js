const doctype = "supplier invoice";
const updateMethod = "sql_accounting_software.sql_accounting_software.doctype.supplier_invoice.supplier_invoice_list.update";

const updateInterval = 10000;
var updateInProgress = false;
var interval;

function isInsideListView() {
    return (cur_page.page.id === `page-List/${doctype}/List`);
}

frappe.listview_settings[doctype] = {

	before_render: function(listview) {
		clearInterval(interval);
		interval = setInterval(function() {
			if (isInsideListView()) {
				if (updateInProgress == false) {
					if (cur_list.get_checked_items().length == 0) {
						cur_list.refresh();	
						return;
					}
					console.log(`${new Date().toLocaleString()} : [-] Paused sync when item is checked.`);
					return;
				}
				console.log(`${new Date().toLocaleString()} : [-] Paused sync when update in progress.`);
				return;
			} else {
				clearInterval(interval);
				console.log(`${new Date().toLocaleString()} : [!] Stopped sync on ${doctype}.`);
			}		
		}, updateInterval);
	},

	refresh: function (listview) {
		updateInProgress = true;
		frappe.call({
            method:"sql_accounting_software.sql_accounting_software.doctype.update.update_all_tables",
            callback:function(r){
                localStorage.clear();
                sessionStorage.clear();
                console.log(`${new Date().toLocaleString()} : ${r.message}`);
                updateInProgress = false;
            },
        });
	},

    onload: function(listview) {
    	console.log("Onload");
  
    	listview.page.set_secondary_action('Sync', function() {
            console.log("Sync is pressed");
            frappe.msgprint("Sync now...");
            frappe.call({
                method: updateMethod,
                callback:function(r){
                	localStorage.clear();
                	sessionStorage.clear();
                    console.log(r.message);
                    // listview.refresh();
                    location.reload();
                },
            })
        }, 'octicon octicon-sync');
    },

    
    
}