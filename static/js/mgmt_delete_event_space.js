/**
* Delete Event Spaces 
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated event space's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
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