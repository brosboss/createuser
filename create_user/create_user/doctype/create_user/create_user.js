// Copyright (c) 2021, !! and contributors
// For license information, please see license.txt

frappe.ui.form.on('Create User', {
	
	// refresh: function(frm) {

	// }
	after_save: function(frm) {	
		frm.set_value("password", "")	
		frm.save()	
		// var email = frm.doc.email
		// var first_name = frm.doc.first_name		
		// var enabled = frm.doc.enabled
		// var password= frm.doc.password
		// var role_profile= frm.doc.role_profile

		//create list of selected roles --------------------------------------------------
		// var selected_roles = []
		// if(frm.doc.orphanage_admin === 1){
		// 	selected_roles.push("Orphanage Admin") 
		// }
		// if(frm.doc.orphanage_recorder === 1){
		// 	selected_roles.push("Orphanage Recorder") 
		// }
		// if(frm.doc.user_creator === 1){
		// 	selected_roles.push("User Creator") 
		// }
		

		// console.log(typeof(selected_roles))
		// //convert array to string
		// selected_roles.join("").toString()


		
		//CREATE OR UPDATE USER RECORDS ------------------------------------------------------------------
		// frappe.db.exists('User', email) .then(records => {
		// 	if(records === true){
		// 		console.log("true")
		// 		//update user record         update_user_record(email, unit,first_name,role_profile):
		// 		frappe.call({					
		// 			method: "orphanage_records.api.update_user_record?enabled="+enabled+"&&email=" + email +"&&first_name="+first_name+"&&password="+password+"&&role_profile="+role_profile,
		// 			freeze:true,
		// 			callback: (response) => {
		// 				console.log(response.message)											
		// 			}			
		// 		})
		// 	}
		// 	if(records === false){	
		// 		console.log("false hhhhhhhhh ")
		// 		//create user record					
		// 		frappe.call({
		// 			method: "orphanage_records.api.create_user?enabled="+enabled+"&&email=" + email +"&&first_name="+first_name+"&&password="+password+"&&role_profile="+role_profile,
		// 			freeze:true,        
		// 			callback: (response) => {
		// 				console.log(response.message)											
		// 			}			
		// 		})	
		// 	}
			
		// })	


		
	},
	update_password : function(frm){
		// var email = frm.doc.email
		// var password= frm.doc.password
		// if(password != ""){
		// 	if(typeof(password) != "undefined"){
		// 		console.log("update password")
		// 		//create user record					
		// 		frappe.call({
		// 			method: "orphanage_records.api.update_password?email="+email+"&&password=" + password,
		// 			freeze:true,
		// 			callback: (response) => {
		// 				console.log(response.message)
		// 				frappe.msgprint("Password Updated")	
		// 				frm.save()	
		// 				frm.refresh()									
		// 			}			
		// 		})

		// 	}
		// }
		
		
	}
});
