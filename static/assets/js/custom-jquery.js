$("#updateProfileFormButton").hide();


function updateProfile() {
  // Get all input elements with the class "form-control"
 $('#user-Update-Profile-Component').removeClass('d-none');
const inputFields = document.querySelectorAll('.form-control');

// Iterate over each input field and remove the "readonly" attribute
inputFields.forEach((input) => {
  input.removeAttribute('readonly');
});
$("#updateProfileFormButton").show();

}


function closeUpdateProfile() {
  // Get all input elements with the class "form-control"
const form = document.querySelector('#updateprofile');
const inputFields = form.querySelectorAll('input');

// Iterate over each input field and set the "readonly" attribute to true
inputFields.forEach((input) => {input.readOnly = true;});
$("#updateProfileFormButton").hide();
$('#user-Update-Profile-Component').addClass('d-none');

}

$("#submitupdateform").on('click', function(){
  $("#updateProfileFormButton").hide();
  const form = document.querySelector('#updateprofile');
  const inputFields = form.querySelectorAll('input');
  inputFields.forEach((input) => {
    input.readOnly = true;
  });
})


function updateProfileView() {
    // Get all input elements with the class "form-control"
 $('#user-Update-Profile-Component').removeClass('d-none');
const inputFields = document.querySelectorAll('.form-control');

// Iterate over each input field and remove the "readonly" attribute

$("#updateProfileFormButton").show();
}