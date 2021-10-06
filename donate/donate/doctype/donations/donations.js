// Copyright (c) 2021, abcd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Donations', {
	// refresh: function(frm) {
	// 	frappe.msgprint(__("hello world"))

	// }
	onload: function(frm){
		frm.set_value("date",frappe.datetime.add_days(frappe.datetime.nowdate()))
	},
	
	on_submit:function(frm) {
		frappe.msgprint(__("Submitted successfully"))
	}
});
