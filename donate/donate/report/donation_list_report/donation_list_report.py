# Copyright (c) 2013, abcd and contributors
# For license information, please see license.txt

import frappe
#from frappe import __


def get_columns():
	return[
		{
			'fieldname':'name',
			'label':('ID'),
			'fieldtype':'Data',
			'width':300	
		},

		{
			'fieldname':'user',
			'label':('User Email'),
			'fieldtype':'Link',
			'width':300	
		},

		{
			'fieldname':'amount',
			'label':('Amount'),
			'fieldtype':'Float',
			'width':300	
		},

	]

def get_data():
	[['1','sps@pps.com',200.90],
	['2','ps@pps.com',2580.90],
	['3','s@pps.com',1500.00]]

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	#data=frappe.get_list("Donations_list",fields=["name","user","amount","status"],filters=filters)
	data=get_data()

	message="Still not working"
	return columns,data,message
