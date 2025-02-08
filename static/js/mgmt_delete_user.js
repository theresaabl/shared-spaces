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