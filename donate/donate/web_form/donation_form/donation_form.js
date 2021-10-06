// frappe.ready(function() {
// 	// bind events here
	
// })

// frappe.web_form.on('date', (field, value) => {
// 	field.set_value(frappe.datetime.add_days(frappe.datetime.nowdate()));
   
// });

// frappe.web_form.after_load = () => {
//     frappe.msgprint('Please fill all values carefully');
// }

frappe.web_form.validate = () => {
    let data = frappe.web_form.get_values();
    if (data.amount < 1000) {
        frappe.msgprint('Value must be more than 1000');
        return false;
    }
};