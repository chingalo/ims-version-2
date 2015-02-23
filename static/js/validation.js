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

//validate create new project form

function validateNewProject(){

	//taking values
	titleOfProject = document.getElementById('title_of_project').value;
	descriptionOfProject = document.getElementById('description_of_project').value;

	//checking for empty form
	if (titleOfProject.length == 0 || titleOfProject == null) {
		document.getElementById('title_of_project').focus();
		return false;
	}

	if (descriptionOfProject.length == 0 || descriptionOfProject == null) {
		document.getElementById('description_of_project').focus();
		return false;
	}
 return true;
}



//validate edit project form

function validateEditProject(){

	//taking values
	titleOfProject = document.getElementById('edited_title_of_project').value;
	descriptionOfProject = document.getElementById('edited_description_of_project').value;

	//checking for empty form
	if (titleOfProject.length == 0 || titleOfProject == null) {
		document.getElementById('edited_title_of_project').focus();
		return false;
	}

	if (descriptionOfProject.length == 0 || descriptionOfProject == null) {
		document.getElementById('edited_description_of_project').focus();
		return false;
	}
 return true;
}