// validate sign up form for emptines

function checkSignUpForm(){

	document.getElementById("password_message").innerHTML = "";
	full_name = document.getElementById('full_name').value;
	email = document.getElementById('email').value;
	mobile_number = document.getElementById('mobile_number').value;
	password = document.getElementById('password').value;
	confirm_password = document.getElementById('confirm_password').value;

	if(full_name == ""){

		document.getElementById('full_name').focus();
		return false;
	}

	if(email == ""){

		document.getElementById('email').focus();
		return false;
	}

	if(mobile_number == ""){

		document.getElementById('mobile_number').focus();
		return false;
	} 
	 
	
	 
	if(password == ""){

		document.getElementById('password').focus();
		return false;
	}


	if(confirm_password == ""){

		document.getElementById('confirm_password').focus();
		return false;
	}

	if(confirm_password != password ){

		document.getElementById('password').focus();
		return false;
	}

	
	 

	
	
	
	 
	 


}