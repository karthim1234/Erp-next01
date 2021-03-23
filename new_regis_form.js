// Copyright (c) 2021, Kartik Mangla and contributors
// For license information, please see license.txt

frappe.ui.form.on('New_Regis_Form', {
	// refresh: function(frm) {
		email:function(frm){
				var email_id = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
				if (email_id.test(frm.doc.email) == false)
				{
					frm.set_value('email', '')
					frappe.throw('Enter valid email_address.');
				}
		},
		mobile_number:function(frm){
				if(frm.doc.mobile_number.length != 10 && frm.doc.mobile_number != ""){
						frm.set_value('mobile_number',"")
						frappe.throw("Invalid  mobile number.")
						}
		}
	// }
});
