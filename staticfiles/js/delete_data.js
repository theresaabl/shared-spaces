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

    const deleteBookingsButtons = document.getElementsByClassName("btn-delete-bookings");
    const deleteBookingsModal = new bootstrap.Modal(document.getElementById("delete-bookings-modal"));
    const deleteBookingsConfirm = document.getElementById("delete-bookings-confirm");

    for (let button of deleteBookingsButtons) {
        button.addEventListener("click", (e) => {
            let bookingId = e.target.getAttribute("booking_id");
            deleteBookingsConfirm.href = `delete_booking/${bookingId}`;
            deleteBookingsModal.show();
        });
    }
});

/**
* Delete Resident Requests
*/

addEventListener("DOMContentLoaded", (e) => {

    const deleteRequestsButtons = document.getElementsByClassName("btn-delete-requests");
    const deleteRequestsModal = new bootstrap.Modal(document.getElementById("delete-requests-modal"));
    const deleteRequestsConfirm = document.getElementById("delete-requests-confirm");

    for (let button of deleteRequestsButtons) {
        button.addEventListener("click", (e) => {
            let residentRequestId = e.target.getAttribute("resident_request_id");
            deleteRequestsConfirm.href = `delete_resident_request/${residentRequestId}`;
            deleteRequestsModal.show();
        });
    }
});
