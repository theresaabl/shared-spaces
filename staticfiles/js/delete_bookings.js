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

    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteModal = new bootstrap.Modal(document.getElementById("delete-modal"));
    const deleteConfirm = document.getElementById("delete-confirm");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let bookingId = e.target.getAttribute("booking_id");
            deleteConfirm.href = `delete_booking/${bookingId}`;
            deleteModal.show();
        });
    }
});
