/* jshint esversion: 11 */

const submitButton = document.getElementById("booking-submit-button");
const title = document.getElementById("booking-title");
const currentURL = window.location.href;

/**
* Edit Bookings 
* - Update title text
* - Updates the submit button's text to "Update".
*/
// check whether booking form is accessed through edit button
if (currentURL.includes('edit_booking')){
    addEventListener("DOMContentLoaded", (e) => {
        title.innerText = "Edit Event Space Booking";
        submitButton.innerText = "Update";
    });
}