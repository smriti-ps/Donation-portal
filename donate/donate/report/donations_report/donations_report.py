# Copyright (c) 2013, abcd and contributors
# For license information, please see license.txt

import frappe

def get_columns():
	columns=[
		{
			'fieldname':'user_id',
			'label':__('ID'),
			'fieldtype':'Data',
			'width':300
			
		}
		
	]
	return columns

def execute(filters=None):
	#columns, data = [], []y