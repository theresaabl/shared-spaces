const submitButton = document.getElementById("manage-event-spaces-submit-button");
const title = document.getElementById("manage-event-spaces-title");
const URL = window.location.href

/**
* Edit Event Spaces from Admin Space 
* - Update title text
* - Updates the submit button's text to "Update".
*/
// check whether event spaces form is accessed through edit button
if (URL.includes('edit-event-space')){
    addEventListener("DOMContentLoaded", (e) => {
        title.innerText = "Edit Event Space"
        submitButton.innerText = "Update";
    });
}