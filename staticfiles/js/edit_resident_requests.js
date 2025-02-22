/* jshint esversion: 11 */

const submitButton = document.getElementById("resident-request-submit-button");
const title = document.getElementById("resident-request-title");
const currentURL = window.location.href;

/**
* Edit Resident Requests
* - Update title text
* - Updates the submit button's text to "Update".
*/
// check whether booking form is accessed through edit button
if (currentURL.includes('edit_resident_request')){
    addEventListener("DOMContentLoaded", (e) => {
        title.innerText = "Edit Request";
        submitButton.innerText = "Update";
    });
}