# -*- coding: utf-8 -*-
# Copyright (c) 2021, !! and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CreateUser(Document):
    def before_save(self):
        # CHECK SITE LIMIT  OR DELETE USER WHEN USER RECORD 
        # [CREATE USER] WHEN USER IS NOT CREATED IN [USER] ------ ??????????????
        create_user(self.enabled, self.email, self.first_name, self.password, self.role_profile )

		# update password when password is set -----------------------------
        if(self.password is not None): 
            if(self.password != ""):
                update_password(self.email, self.password)
           


@frappe.whitelist()
def create_user(enabled, email, first_name, password, role_profile ):  
    if frappe.db.exists("User", email):
        update_user_record(enabled, email, first_name, password, role_profile)
        
    
    if not frappe.db.exists("User", email):
        user = frappe.get_doc({
			"doctype": "User",
			"email": email,
			"first_name": first_name,
			"send_welcome_email": 0,
			"enabled": enabled
		})
        user.insert(ignore_permissions=True)
        frappe.db.commit()
        set_role_profile(email, role_profile)  
        frappe.db.commit()

@frappe.whitelist()
def update_password(email, password): 
    doc = frappe.get_doc("User", email)
    doc.new_password = password     
    doc.save(ignore_permissions=True)     
    frappe.db.commit() 
    
    
@frappe.whitelist()
def set_role_profile(email, role_profile): 
    doc = frappe.get_doc("User", email)
    doc.role_profile_name = role_profile 
    doc.save(ignore_permissions=True)     
    frappe.db.commit()  
    set_to_system_user(email)
    frappe.db.commit() 

@frappe.whitelist()
def set_to_system_user(email): 
    doc = frappe.get_doc("User", email)
    doc.user_type = "System User"  
    doc.save(ignore_permissions=True)     
    frappe.db.commit() 
    
    
# TO UPDATE USER
@frappe.whitelist()  
def update_user_record(enabled, email, first_name, password, role_profile):
    doc = frappe.get_doc("User", email)
    doc.enabled = enabled 
    doc.email = email 
    doc.first_name = first_name 
    doc.new_password = password  
    doc.role_profile_name = role_profile 
    doc.module_profile ="No Module Allowed"
    doc.save(ignore_permissions=True)
    frappe.db.commit() 
    

