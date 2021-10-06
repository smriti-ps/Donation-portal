// Copyright (c) 2016, abcd and contributors
// For license information, please see license.txt
/* eslint-disable */

//const { options } = require("superagent");

frappe.query_reports["Donation_list_report"] = {
	"filters": [
		{
			'fieldname':'status',
			'label':('Donation Staus'),
			fieldtype: 'Select',
			options:['',
				'Draft',
				'Completed'

			],
			'width':100,
			default:'',
		},
		
		{
			'fieldname':'from',
			'label':('From Date'),
			fieldtype: 'Date',
			'width':100,
			default: frappe.datetime.year_start()
		},

		{
			'fieldname':'to',
			'label':__('Till Date'),
			fieldtype: 'Date',
			'width':100,
			default: frappe.datetime.year_end()
		},

		{
			'fieldname':'user',
			'label':('User Email'),
			fieldtype: 'Link',
			'options':'User',
			'width':100,
			default: ''
		},
	]
};
