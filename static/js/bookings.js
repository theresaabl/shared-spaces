const submitButton = document.getElementById("bookingSubmitButton");
const URL = window.location.href

/**
* - Updates the submit button's text to "Update".
*/

if (URL.includes('edit_booking')){
    addEventListener("DOMContentLoaded", (e) => {
        submitButton.innerText = "Update";
    });
}