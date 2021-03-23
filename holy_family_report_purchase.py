# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import has_common
import json
from six import StringIO, string_types

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_data(filters):
	query_data = frappe.db.sql("""SELECT name from `tabPurchase Invoice` where docstatus=1 and grand_total>10000 and '{0}'""".format(get_filters_codition(filters)),as_list=True)
	
	return query_data



def get_filters_codition(filters):
	conditions = "1=1"
	if filters.get("from_date"):
		conditions += " and start_date >= '{0}'".format(filters.get('from_date'))
	if filters.get("to_date"):
		conditions += " and start_date <= '{0}'".format(filters.get('to_date'))
	return conditions

def get_columns():
	return	[
		{
			"label": _("PI Name"),
			"fieldname": "name",
			"fieldtype": "Data",
			"width": 120
		}
	]
