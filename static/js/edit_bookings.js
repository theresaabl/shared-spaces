const submitButton = document.getElementById("booking-submit-button");
const title = document.getElementById("booking-title");
const URL = window.location.href

/**
* Edit Bookings 
* - Updates the submit button's text to "Update".
*/
// check whether booking form is accessed through edit button
if (URL.includes('edit_booking')){
    addEventListener("DOMContentLoaded", (e) => {
        title.innerText = "Edit Event Space Booking"
        submitButton.innerText = "Update";
    });
}