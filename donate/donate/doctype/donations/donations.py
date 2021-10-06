# Copyright (c) 2021, abcd and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
import frappe
import json

class Donations(Document):
	def autoname(self):
		self.name=self.user


	def after_insert(self):
		created_division=self.division
		created_amount=self.amount
		created_user=self.user
		all_division=frappe.db.get_value("Employee Profile",filters={"division":created_division})
		all_emails = frappe.db.sql("SELECT name FROM `tabEmployee Profile` where division= 'Mumbai'", as_dict=1)
		message="Thank you for your contribution!!!!:)"
		msg=self.division
		send_mail(all_division,created_amount,created_user)
		frappe.msgprint(message+str(all_division))

def send_mail(all_division,amount,user):

	# frappe.sendmail() function not working properly.
	recipients=[]
	for mails in all_division:
		recipients.append(mails[0])
	#recipients=['smriti@chezuba.net']
	frappe.sendmail(
		recipients=recipients,
		sender='factual.opinionist@gmail.com',
		message='{} donated {} amount'.format(user,amount)
	)
	



@frappe.whitelist()
def donation_entry(donation_detail,doc_name):
	donation_detail=json.loads(donation_detail)
	doc_name=json.loads(doc_name)

	# raw_date=donation_detail['date']   # dd-mm-yy format
	# modified_date=raw_date.split('-')
	# modified_date[0],modified_date[-1]=modified_date[-1],modified_date[0]
	# date='-'.join(modified_date) #yy-mm-dd format

	if frappe.session.user != doc_name["user_name"]:
		# current user is trying to update other users profile
		return {"error": "You are not allowed to visit this page"}
	try:
		# if not donation_detail["amount"] and  not donation_detail["date"]:
		new_donation=frappe.get_doc({'doctype':'Donations',
									'user':donation_detail["user"],
									'amount':donation_detail["amount"],
									'date':donation_detail["date"]})
		new_donation.insert()
		frappe.db.commit()
		return {"success":"Thank you for your contribution"}
	except:
		return {"error":"Error while completing the request"}