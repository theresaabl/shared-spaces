/**
* Delete Users 
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated user's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

addEventListener("DOMContentLoaded", (e) => {

    const deleteUsersButtons = document.getElementsByClassName("btn-delete-users");
    const deleteUsersModal = new bootstrap.Modal(document.getElementById("delete-users-modal"));
    const deleteUsersConfirm = document.getElementById("delete-users-confirm");

    for (let button of deleteUsersButtons) {
        button.addEventListener("click", (e) => {
            let userId = e.target.getAttribute("user_id");
            deleteUsersConfirm.href = `delete-user/${userId}`;
            deleteUsersModal.show();
        });
    }
});


/**
* Delete Event Spaces 
*/

addEventListener("DOMContentLoaded", (e) => {

    const deleteSpacesButtons = document.getElementsByClassName("btn-delete-event-space");
    const deleteSpacesModal = new bootstrap.Modal(document.getElementById("delete-event-space-modal"));
    const deleteSpacesConfirm = document.getElementById("delete-event-space-confirm");

    for (let button of deleteSpacesButtons) {
        button.addEventListener("click", (e) => {
            let spaceId = e.target.getAttribute("space_id");
            deleteSpacesConfirm.href = `delete-event-space/${spaceId}`;
            deleteSpacesModal.show();
        });
    }
});


/**
* Delete Event Space Bookings 
*/

addEventListener("DOMContentLoaded", (e) => {

    const deleteBookingsButtons = document.getElementsByClassName("btn-mgmt-delete-booking");
    const deleteBookingsModal = new bootstrap.Modal(document.getElementById("mgmt-delete-booking-modal"));
    const deleteBookingsConfirm = document.getElementById("mgmt-delete-booking-confirm");

    for (let button of deleteBookingsButtons) {
        button.addEventListener("click", (e) => {
            let bookingId = e.target.getAttribute("booking_id");
            deleteBookingsConfirm.href = `delete-booking/${bookingId}`;
            deleteBookingsModal.show();
        });
    }
});