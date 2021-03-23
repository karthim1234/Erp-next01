# -*- coding: utf-8 -*-
# Copyright (c) 2021, Kartik Mangla and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class New_Regis_Form(Document):
		def on_submit(doc):
				print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",doc.email)
				user_doc = frappe.new_doc('User')
				user_doc.email = doc.email
				user_doc.first_name = doc.name
				user_doc.save(ignore_permissions=True)
				frappe.db.commit()
