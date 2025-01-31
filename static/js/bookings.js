// for event_space_booking.html
const submitButton = document.getElementById("booking-submit-button");
const title = document.getElementById("booking-title");
const URL = window.location.href

// for resident_space.html
const deleteModal = new bootstrap.Modal(document.getElementById("delete-modal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("delete-confirm");


/**
* Edit Bookings 
* - Updates the submit button's text to "Update".
*/
if (URL.includes('edit_booking')){
    addEventListener("DOMContentLoaded", (e) => {
        title.innerText = "Edit Event Space Booking"
        submitButton.innerText = "Update";
    });
}

/**
* Delete Bookings 
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated booking's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
addEventListener("DOMContentLoaded", (e) => {
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let bookingId = e.target.getAttribute("booking_id");
            deleteConfirm.href = `delete_booking/${bookingId}`;
            deleteModal.show();
        });
    }
});