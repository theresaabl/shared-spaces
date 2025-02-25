# [SharedSpaces](https://shared-spaces-f588831ae867.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/TheresaAbl/shared-spaces)](https://www.github.com/TheresaAbl/shared-spaces/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/TheresaAbl/shared-spaces)](https://www.github.com/TheresaAbl/shared-spaces/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheresaAbl/shared-spaces)](https://www.github.com/TheresaAbl/shared-spaces)

A website for a community living space called SharedSpaces. SharedSpaces is a living community providing a space to live, a space to work and a space for community. The website shows concise and inviting information about the living community and provides a contact form for users who would like to join the community. Residents of the SharedSpaces community can register for an account and book event spaces available in the community, as well as send maintenance requests and messages to the administrators. SharedSpaces administrators have access to a front end admin site where they can manage user accounts, event spaces, event space bookings and maintenance requests as well as messages from residents, and contact messages sent through the contact form.

This is a site where everyone in the SharedSpaces community (or interested to join) can find what they need in one place and in a simple and pleasant way, whether they are general users, registered residents or administrators.

Live Site - [SharedSpaces](https://shared-spaces-f588831ae867.herokuapp.com/)

![screenshot](documentation/responsiveness/amiresponsive.png)

source: [shared-spaces amiresponsive](https://ui.dev/amiresponsive?url=https://shared-spaces-f588831ae867.herokuapp.com)

> [!IMPORTANT]
> - Any User signing up on this site is automatically set to inactive and will need to be approved by the admins before signing in!
> - This site has an Admin Front End Page.

## UX

### The 5 Planes of UX

#### 1. Strategy Plane
##### Purpose
- Provide SharedSpaces residents a place to participate in the community, use shared event spaces and interact with the admins to make them feel like they belong to something bigger
- Provide SharedSpaces administrators a place to manage all the data they need to manage in a very user friendly and quick and simple way
- Offer guest users a friendly and well organised space to get information about the community and contact the administrators or send a request to join the community

##### Primary User Needs
- SharedSpaces residents need a seamless tool to book event spaces and manage the bookings, as well as send maintenance requests and messages and manage those
- SharedSpaces administrators need a seamless tool to manage user accounts, event spaces, event space bookings, resident maintenance requests and messages, as well as contact messages from general users
- Guests need the ability to browse the site, get information and contact administrators without registration.

##### Business Goals
- Build a sense of community within the residents by keeping them happy with the possibilities to interact and use shared event spaces in the community.
- Ensure easy data management for admins.
- Show off the advantages of the living community in an inviting way to the general public

#### 2. Scope Plane
##### Features
- A full list of [Features](#features) can be viewed in detail below.

##### Content Requirements
- User account management (Users: create, Admins: preview, update (activate, deactivate, give and remove admin status) and delete).
- Event Space management (Registered users: preview, Admins: create, update, delete and preview).
- Event space booking management (Registered users: create, update, delete, preview, Admins: approve, deny, delete and preview).
- Maintenance requests and other messages management (Registered users: create, update, delete, preview, Admins: update (change status - open, in progress, closed), delete and preview).
- Contact messages (from contact form) management (Users: create, Admins: preview, update (change status - processed) and delete).
- User account features (register, log in, logout, account inactive page).
- Notification system for when any data is changed.
- 404 error page for lost users.

#### 3. Structure Plane
##### Information Architecture
- **Navigation Menu**:
  - Links to Home, About (section on home page), Contact, Resident Space (dashboard accessible for registered and activated users), Admin Space (only visible for admins), Login/Register (or Logout)
- **Hierarchy**:
  - Hero Section and highlights about the community prominently displayed for easy browsing.
  - Easily visible about section
  - Clear call-to-action buttons to request to join the SharedSpaces community leading to the contact page
  - Clear and simple contact form
  - Resident Space available for confirmed residents, anyone who uses it knows that it is there. Within the resident space:
      - Prominently displayed calls to action to book event space or send a request
      - Display of all bookings and requests available for that user
  - Admin space only visible for admins and they will know what they are looking for
    - Access to manage all data needed

##### User Flow
1. Guest users browse home and about page content → see 'join' buttons and get to contact page → send a contact message.
2. Guest users register for an account → wait for admins to approve them (if they are confirmed residents of the living community).
3. Registered but not activated users try to log in → see the account inactive page.
4. Registered users submit a booking or request or message → receive a pending approval notification.
5. Registered users edit a booking or request or message → receive a pending approval notification.
6. Admins create, update, and manage event spaces → registered users can see that and book accordingly.
7. Admins manage user accounts → registered users can log in or not.
8. Admins manage event space bookings and resident requests → registered users can see the result and react accordingly.

#### 4. Skeleton Plane
##### Wireframe Suggestions
- A full list of [Wireframes](#wireframes) can be viewed in detail below.

#### 5. Surface Plane
##### Visual Design Elements

The goal of the design was to make a very friendly, vibrant and inviting website that has a clean and modern look and is very intuitive to navigate. To achieve this goal the following colour scheme and typography was used:

- **[Colours](#colour-scheme)**: see below.
- **[Typography](#typography)**: see below.

### Colour Scheme

I used [coolors.co](https://coolors.co/324495-f6ae2d-f26419-ffffff-212529) to generate my color palette. The goal was a very clean and simple, but still vibrant and inviting look. I used shades of yellow, orange and blue to style the highlights throughout the site (e.g. headings, borders, buttons etc.) which gives a bright and vibrant look, the rest is kept very simple with white background and dark-grey text, where the dark grey is the standard bootstrap body text color.

![screenshot](documentation/coolors.png)

- `#f6ae2d` Yellow: highlights and buttons
- `#f26419` Orange: highlights and buttons
- `#324495` Blue: highlights, buttons and links
- `#212529` Dark-grey: all text (except links or text on darker backgrounds is white)
- `#ffffff` White: background color.

I defined my color variables in my [CSS file](static/css/style.css) as follows:

```
:root {
    --my-blue: #324495;
    --my-blue-active: #24316b;
    --my-yellow: #f6ae2d;
    --my-yellow-active: #cd9326;
    --my-orange: #f26419;
    --my-orange-active: #d16023;
  }
```

where I also included slightly darker shades for active buttons and links.

### Typography

- [Alumni Sans Pinstripe](https://fonts.google.com/specimen/Alumni+Sans+Pinstripe) was used for the logo and the word SharedSpaces in general, this font looks geometrical and modern as well as light, which fits with the building theme.
- [Quicksand](https://fonts.google.com/specimen/Quicksand) was used for all other text, it is fitting with a modern but friendly style.
- [Font Awesome](https://fontawesome.com) icons were used to help visualize some of the data displayed, such as on the event spaces list pages in the resident and admin spaces or the user accounts page in the admin space.

## User Stories

### [EPIC: User Authentication](https://github.com/theresaabl/shared-spaces/issues/1)

As a Confirmed Resident I can register an account so that I can access a resident dashboard.

User Stories:
- [As a Site User I can sign up for an account](https://github.com/theresaabl/shared-spaces/issues/2) so that I can request to get access to a resident dashboard.
- [As a Site Administrator I can see all requests for a new user account](https://github.com/theresaabl/shared-spaces/issues/3) so that I can confirm accounts for SharedSpaces residents only.
- [As a Confirmed Resident I can login and logout of my account](https://github.com/theresaabl/shared-spaces/issues/4) so that I can access a resident dashboard.
- [As a Site User I can see a message when login does not work (yet)](https://github.com/theresaabl/shared-spaces/issues/5) so that I can know whether my account has been approved yet or not.

### [EPIC: Resident Dashboard](https://github.com/theresaabl/shared-spaces/issues/7)

As a Confirmed Resident I can get an email notification once my account is confirmed so that I can know immediately when I get access to the resident dashboard.

User Stories:

- [As a Confirmed Resident I can book an event space](https://github.com/theresaabl/shared-spaces/issues/11) so that I can make use of the shared spaces in my community.
- [As a Confirmed Resident I can see my event space bookings on the dashboard](https://github.com/theresaabl/shared-spaces/issues/12) so that I can manage them.
- [As a Confirmed Resident I can see my sent requests and messages on the dashboard](https://github.com/theresaabl/shared-spaces/issues/13)  so that I can manage them.
- [As a Confirmed Resident I can see a page with a list of all available event spaces](https://github.com/theresaabl/shared-spaces/issues/14)  so that I can decide which one I want to book.
- [As a Confirmed Resident I can access a calender which allows me to pick dates in the future when booking event spaces](https://github.com/theresaabl/shared-spaces/issues/17) so that I can easily pick a date.
- [As a Confirmed Resident I can send a maintenance request or other message to the admins](https://github.com/theresaabl/shared-spaces/issues/27) so that I can get in touch in case I have any issues or suggestions.

### [EPIC: Main Site](https://github.com/theresaabl/shared-spaces/issues/8)

As a Site User I can see the main SharedSpaces site so that I can read information about the community living space and contact someone.

User Stories:
- [As a Site User I can see the home page](https://github.com/theresaabl/shared-spaces/issues/18) so that I know what this site is about.
- [As a Site User I can see the about section](https://github.com/theresaabl/shared-spaces/issues/19) so that I can read more about the shared spaces community living.
- [As a Site User I can see the contact page](https://github.com/theresaabl/shared-spaces/issues/20) so that I can contact the community admins.
- [As a Site User I can fill in a contact form](https://github.com/theresaabl/shared-spaces/issues/21) so that I can contact the community administrators.
- [As a Site User I can see an error 404 page](https://github.com/theresaabl/shared-spaces/issues/40) so that I know when a page does not exist.
 

### [EPIC: Admin Frontend Page](https://github.com/theresaabl/shared-spaces/issues/9)

As a Site Administrator I can access data from a frontend page so that I can create, read, edit and delete data from the database in a simple and pleasant way.

User Stories:
- [As a Site Administrator I can access a front-end admin page](https://github.com/theresaabl/shared-spaces/issues/26) so that I can manage all data from a user friendly front-end page instead of the admin panel.
- [As a Site Administrator I can manage user accounts](https://github.com/theresaabl/shared-spaces/issues/35) so that I can approve or deny new users depending on whether they are confirmed residents of the SharedSpaces community or not.
- [As a Site Administrator I can read all contact form submissions](https://github.com/theresaabl/shared-spaces/issues/22) so that I can process them.
- [As a Site Administrator I can manage event space booking requests from confirmed residents](https://github.com/theresaabl/shared-spaces/issues/23) so that I can confirm or deny bookings.
- [As a Site Administrator I can manage maintanance or other requests from confirmed residents](https://github.com/theresaabl/shared-spaces/issues/24) so that I can read their requests and take further action.
- [As a Site Administrator I can manage the list of event spaces available as well as the details about them](https://github.com/theresaabl/shared-spaces/issues/25) so that I can show up to date information on the website.


## Wireframes

I have used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes. Note that even though the site was designed mobile first, I chose to create the wireframes for desktop devices, since the design very naturally generalises to other devices. The site was designed in a way that made the adaptations for mobile devices almost obvious.

Any differences between the wireframes and the final website are due to creative decisions in the development process. For example, I decided to omit the map on the contact page to keep the page cleaner and focus on the most important content which is the contact form. External users do not need to go to the living community unless they first request to join it. Further, I omitted the social media icons for a cleaner look and because the living community would be more likely to have internal communications instead of social media, instead I added an external link to GitHub in the footer. 

| Page | Wireframe |
|---|---|
| Home | ![Sreenshot](documentation/wireframes/home.png) |   
| About | ![Sreenshot](documentation/wireframes/about.png) |   
| Contact | ![Sreenshot](documentation/wireframes/contact.png) |
| Resident Space | ![Sreenshot](documentation/wireframes/resident_dashboard.png) |   
| Event Spaces | ![Sreenshot](documentation/wireframes/event_spaces.png) |   
| Event Space Booking | ![Sreenshot](documentation/wireframes/event_space_booking.png) |   
| Request Submission | ![Sreenshot](documentation/wireframes/request_submission.png) |   
| Admin Page | ![Sreenshot](documentation/wireframes/admin_page.png) |   


## Features

> [!IMPORTANT]
> - Any User signing up on this site is automatically set to inactive and will need to be approved by the admins before signing in!
> - This site has an Admin Front End Page.

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. The registration is customized so that users are automatically set to inactive upon signup, they are then redirected to the account inactive page (see below) until the admin has approved the account (see below). This is necessary so that only residents of the community can get a user account. The form is also customized to include the full name and make the email required, so that residents can be identified by the admins. | ![screenshot](documentation/features/signup.png)![screenshot](documentation/features/signup-2.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts if they are approved. | ![screenshot](documentation/features/sign-in.png) |
| Account Inactive Page | The login process is customized such that users who have registered for an account but have not yet been activated by the admins are redirected to the account inactive page upon signup and when trying to login. | ![screenshot](documentation/features/account-inactive.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/signout.png) |
| Navbar | The navigation bar on top of the page contains a SharedSpaces logo with a link to the homepage, as well as link to the other pages and authentication function. The navbar collapses to a dropdown menu on smaller devices and there are differences for different users. For registered users the resident space link is highlighted and the admin space link is only available for admins. | ![screenshot](documentation/features/navbar-unauthenticated.png)![screenshot](documentation/features/navbar-user.png)![screenshot](documentation/features/navbar-admin.png)![screenshot](documentation/features/navbar-admin-galaxy.jpg) |
| Home | The homepage displays a hero section with a hero image as well as the highlights of the community. | ![screenshot](documentation/features/hero-section.png)![screenshot](documentation/features/highlights-section.png) |
| About | The about section on the homepage gives some more information about the community and includes pictures. | ![screenshot](documentation/features/about-header.png)![screenshot](documentation/features/about-section-1.png)![screenshot](documentation/features/about-section-2.png) |
| 'Requet to Join SharedSpaces Community here' buttons | Below the highlights secton and the about section is a button for general users to request to join the community, this is an inviting and prominent button that leads to the contact form. | ![screenshot](documentation/features/request-to-join-button.png) |
| Contact Page | The contact page contains a header image and a contact form. | ![screenshot](documentation/features/contact-header.png)![screenshot](documentation/features/contact-form.png) |
| Send Contact Message | On the contact page users can send a contact message to the admins without authentication. They can check a box to indicate whether they want to join the SharedSpaces community or not. | ![screenshot](documentation/features/success-contact-message-submitted.png) |
| Footer | The footer displays the copyright and the sharedspaces logo link to my GitHub page. | ![screenshot](documentation/features/footer.png) |
| Resident Space | Authenticated visitors can can access a personal resident dashboard. Where they can see event spaces, their own event space bookings and resident requests. They can also make new bookings and requests and edit and delete them. The bookings are sorted into pending, approved, denied and past bookings and the maintenance requests and messages are sorted into open, in progress and closed requests. | ![screenshot](documentation/features/dashboard.png)![screenshot](documentation/features/dashboard-bookings-requests-lenovo.png) |
| Resident Space for unauthenticated Users | Unauthenticated users who click on the resident space link get a screen that tells them to sign in. | ![screenshot](documentation/features/resident-space-not-signed-in.png) |
| Event Spaces List | From the resident space users can access a page that shows all available event spaces and each space has a button to book the event space directly. This opens the book event space form with prefilled event space field (see below). | ![screenshot](documentation/features/dashboard-event-spaces-lenovo.png)![screenshot](documentation/features/book-this-space-button.png) |
| Event Space Booking | The event space booking form allows registered users to book event spaces. The form is validated and ensures that there are no bookings at the same time in the same space, that there is at least one hour between bookings and that each booking has a duration of at least one hour where the end time is after the start time. Specific error messages are displayed, as well as a success message in case the booking was successful. The booking then needs to be approve by the admin and is now pending, this is stated in the success message. | ![screenshot](documentation/features/book-event-space-form.png)![screenshot](documentation/features/successful-booking-message.png)![screenshot](documentation/features/booking-error-duplicate.png)![screenshot](documentation/features/booking-error-end-time.png)![screenshot](documentation/features/booking-error-short-duration.png) |
| Date Picker in event space booking form | In the booking form date field, a date picker calendar is available that only allows future dates to be selected. A time picker is available too. | ![screenshot](documentation/features/date-picker-tab.jpg)![screenshot](documentation/features/time-picker-tab.jpg) |
| Event Space Booking for a specific event space | The form is prefilled with a specific event space, this is accessed from the event spaces page (see above). | ![screenshot](documentation/features/book-this-space-prefilled.png) |
| Submit a Request | The submit a request form allows registered users to submit maintenance requests or general messages to the admins, they can check a box whether it is urgent or not. The form is validated and success or fail messages are displayed. When the request went through it is set to open and the admins can change the status. | ![screenshot](documentation/features/submit-request.png)![screenshot](documentation/features/successful-maintenance-request.png)![screenshot](documentation/features/successful-message-submit.png) |
| Edit Event Space Booking | Each booking of a user displayed in their resident space has an edit button which leads to a prefilled edit event space form. This form is again validated like when originally booked. The status is set to pending again unless only the occasion and the notes are changed. A success message is displayed. The title and the submit button change to edit and update (this is the same in all edit forms throughout the site). There is a message in case no changes were made. It is made sure of that one cannot edit bookings from other users or past bookings. | ![screenshot](documentation/features/edit-event-space-booking-lenovo.png)![screenshot](documentation/features/edit-form-update-button.png)![screenshot](documentation/features/success-update-booking.png)![screenshot](documentation/features/success-update-booking-status-stays.png)![screenshot](documentation/features/no-changes-made-booking.png)![screenshot](documentation/features/error-edit-other-users-booking.png)![screenshot](documentation/features/error-edit-past-booking.png) |
| Delete Event Space Booking | Each booking of a user displayed in their resident space has a delete button. When clicking the button a confirmation modal opens to ask the user whether they are certain they want to delete the booking. If the user clicks on Delete again the booking is deleted and a success message is shown. It is made sure of that one cannot delete bookings from other users or past bookings. | ![screenshot](documentation/features/delete-booking-confirmation.png)![screenshot](documentation/features/booking-delete-message.png)![screenshot](documentation/features/error-edit-other-users-booking.png)![screenshot](documentation/features/error-delete-past-booking.png) |
| Edit a Request | Each maintenance request or message of a user displayed in their resident space has an edit button which leads to a prefilled edit request form. If the form is valid the status is set to open again and a success message is displayed. There is a message in case no changes were made. It is made sure of that one cannot edit requests from other users. | ![screenshot](documentation/features/edit-request-lenovo.png)![screenshot](documentation/features/success-update-request.png)![screenshot](documentation/features/no-changes-made-request.png)![screenshot](documentation/features/request-error-other-users-request.png) |
| Delete a request | maintenance request or message of a user displayed in their resident space has a delete button. When clicking the button a confirmation modal opens to ask the user whether they are certain they want to delete the request. If the user clicks on Delete again the request is deleted and a success message is shown. It is made sure of that one cannot delete requests from other users.  | ![screenshot](documentation/features/delete-request-confirmation.png)![screenshot](documentation/features/request-delete-message.png)![screenshot](documentation/features/request-error-other-users-request.png) |
| Return to Resident Space Button | On the event spaces list and the booking and resident request form pages, there is a 'return to resident space' button that leads back to the resident space. | ![screenshot](documentation/features/return-to-dashboard-button.png) |
| Admin Space | Authenticated users with staff status can access the admin space through a highlighted link in the navbar (see above). The admin space main site displays the different data that can be managed and has buttons with links to each of them. All pages within the admin space are only available to staff users! | ![screenshot](documentation/features/admin-space.png) |
| Manage User Accounts | On the user accounts page all users are shown and sorted into inactive, confirmed residents(active users) and community administrators (admins with staff status). | ![screenshot](documentation/features/user-accounts-lenovo.png)![screenshot](documentation/features/user-accounts-inactive.png)![screenshot](documentation/features/user-accounts-confirmed.png)![screenshot](documentation/features/user-accounts-admin.png) |
| Activate/Deactivate User Accounts | Inactive user accounts can be activated with a button click and active users can be deactivated with a button click. It is made sure off that the admin can not accidentally delete their own account. | ![screenshot](documentation/features/user-activated.png)![screenshot](documentation/features/user-deactivated.png)![screenshot](documentation/features/admin-deactivate-own-account.png) |
| Give/Remove Admin Status to User | Confirmed residents' user accounts can be given admin status with a button click and admins' accounts can admin status be removed from with a button click. It is made sure off that the admin can not accidentally remove their own admin status. | ![screenshot](documentation/features/add-admin-status.png)![screenshot](documentation/features/remove-admin-status.png)![screenshot](documentation/features/admin-remove-own-admin-status.png) |
| Delete User Account | Admins can delete user accounts (except their own). Again a confirmation modal is shown before a success message. | ![screenshot](documentation/features/user-delete-confirmation.png)![screenshot](documentation/features/delete-user-message.png)![screenshot](documentation/features/admin-delete-own-account.png) |
| Manage Event Spaces | On the event spaces page all event spaces are shown and there is an add event space button to access the event space form. There are also edit and delete buttons for each event space. | ![screenshot](documentation/features/event-spaces-and-add-button.png)![screenshot](documentation/features/event-spaces-edit-delete.png) |
| Add an Event Space | Admins can add new event spaces which are available in the community. An image can be uploaded as well, and the form is validated. A success message or error message is shown | ![screenshot](documentation/features/admin-add-event-space.png)![screenshot](documentation/features/add-event-space-message.png) |
| Edit Event Space | When clicking on the edit button on an event space, the event space form opens and is prefilled. The form is again validated and a success message displayed. If no changes are made a message indicates that. | ![screenshot](documentation/features/edit-event-space.png)![screenshot](documentation/features/update-event-space-message.png)![screenshot](documentation/features/no-changes-made-event-space.png) |
| Delete Event Space | When clicking on the delete button on an event space, the confirmation modal opens and if confirmed a success message is shown. | ![screenshot](documentation/features/delete-event-space-confirmation.png)![screenshot](documentation/features/delete-event-space-message.png) |
| Manage Event Space Bookings | On the event space bookings page all event space bookings from all users are shown and sorted into pending, approved, denied and past bookings. | ![screenshot](documentation/features/admin-bookings-pending.png)![screenshot](documentation/features/admin-bookings-approved.png)![screenshot](documentation/features/admin-bookings-denied.png)![screenshot](documentation/features/admin-bookings-past.png) |
| Approve/Deny Event Space Booking | Pending and denied bookings can be approved with a button click and pending or approved bookings can be denied with a button click. A success message is shown. Past bookings cannot be changed. | ![screenshot](documentation/features/approve-booking-message.png)![screenshot](documentation/features/deny-booking-message.png) |
| Delete Event Space Booking | Admins can delete event space bookings (also past ones). Again a confirmation modal is shown before a success message. | ![screenshot](documentation/features/delete-booking-confirmation.png)![screenshot](documentation/features/booking-delete-message.png) |
| Manage Resident Requests | On the resident requests page all maintenance requests and messages from all users are shown and sorted into open, in progress and closed. | ![screenshot](documentation/features/admin-requests-open.png)![screenshot](documentation/features/admin-requests-in-progress.png)![screenshot](documentation/features/admin-requests-closed.png) |
| Set status to open/in progress/closed for Resident Request | Open requests can be set to in progress or closed, in progress requests can be set to closed and closed requests can be set to in progress by clicking reopen. All with one button click. Success messages are shown. | ![screenshot](documentation/features/message-request-closed.png)![screenshot](documentation/features/message-in-progress.png) |
| Delete Resident Request | Admins can delete resident requests. Again a confirmation modal is shown before a success message. | ![screenshot](documentation/features/delete-request-confirmation.png)![screenshot](documentation/features/request-delete-message.png) |
| Manage Contact Messages | On the resident requests page all contact messages sent from external users through the contact form are shown and sorted into open and processed (similar to unread and read in emails). | ![screenshot](documentation/features/contact-messages-open.png)![screenshot](documentation/features/contact-messages-processed.png) |
| Set status to Processed for Contact Message | Open messages can be set to processed to indicate that they have been dealt with. | ![screenshot](documentation/features/success-contact-message-processed.png) |
| Delete Contact Message | Admins can delete contact messages. Again a confirmation modal is shown before a success message. | ![screenshot](documentation/features/delete-contact-message-confirmation.png)![screenshot](documentation/features/delete-contact-message.png) |
| Return to Admin Space Button | Each of the admin space pages has a 'return to admin space' button that link back to the main admin space page. | ![screenshot](documentation/features/back-to-admin-button.png) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. |  |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/error-404-page.png) |

### Future Features

[![GitHub issues](https://img.shields.io/github/issues/theresaabl/shared-spaces)](https://www.github.com/theresaabl/shared-spaces/issues) 

Some interesting future features are documented in the open github issues as epics and user stories.

There are many potential interesting future features for this project, some examples are:

- **Residents Message Board and User Profiles**: A message board available in the resident space where resident can see other residents' messages, comment and post on their own. This would also include user profiles similar to a private small social media platform for the community.
- **Manage maintenance requests and messages within the Site**: It would be great if the admin could answer to requests from residents directly in the admin space and this could be displayed in the users resident space.
- **Send email notification**: It would be a great future feature to send email notifications once the admins have approved and activated a users account. Further, email notifications would be useful whenever the status of a booking or request changes, e.g. is confirmed or denied etc.
- **Show availability in calender when booking event spaces**: It would be very useful if users can see the availability of an event space in the date picker and time picker in real time when booking an event space.
- **Option to filter data in resident space and admin space**: It would be very useful if users could filter data displayed in the resident space or admin space by status or user or date etc. Currently admins can do that in the django admin panel. In the front end the data is sorted into categories but all it displayed.
- **Search functionality**: Implement search functionality for resident space and admin space data.


## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. Help write the home and about text. |
| [![Cloudconvert](https://img.shields.io/badge/Cloudconvert-grey?logo=adobecreativecloud&logoColor=B53836)](https://cloudconvert.com/webp-converter) | Convert all images to webp for faster website. |
| [![Tinypng](https://img.shields.io/badge/Tinypng-grey?logo=foodpanda&logoColor=7EB631)](https://tinypng.com) | Compress images for faster website. |
| [![Favicon](https://img.shields.io/badge/Favicon-grey?logo=fi&logoColor=209CEE)](https://favicon.io/emoji-favicons/atom-symbol) | Generate favicon for the website. |


## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.
I used [Draw.io](https://draw.io) to create my ERDs:

![screenshot](documentation/diagrams/models.webp)

I created four custom models, on for event spaces (EventSpace), one for event space bookings (EventSpaceBooking), one for resident requests (ResidentRequest) and one for contact messages (ContactMessage). The EventSpaceBooking model has a customized clean method to make sure that only valid data is entered to the database, it checks that there are no two bookings at the same time in the same space and that at least one hour is between different bookings. It also checks that the end time of the booking is after the start time and that there is at least 1 hour between start and end time.

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/theresaabl/shared-spaces/projects) served as an Agile tool for this project. Through it, EPICs, User Stories (with acceptance criteria, tasks, MoSCoW prioritisation and story points), issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board. I planned my project in five milestones (iteration 1 - 5) with one iteration per week (1.5 for iteration 5) and created one project board per milestone. Note that I left the projects open for the purpose of the assessment for better visibility. I am aware that usually I would close them when they are done.

Here are screenshots of the project boards, note that I took them once the iteration was done and all the tasks where finished.

| Project | Screenshot |
|---|---|
| Iteration 1 | ![Sreenshot](documentation/agile/project-iteration1.png) |   
| Iteration 2 | ![Sreenshot](documentation/agile/project-iteration2.png) |   
| Iteration 3 | ![Sreenshot](documentation/agile/project-iteration3.png) |
| Iteration 4 | ![Sreenshot](documentation/agile/project-iteration4.png) |   
| Iteration 5 | ![Sreenshot](documentation/agile/project-iteration5.png) |     

### GitHub Issues

[GitHub Issues](https://www.github.com/theresaabl/shared-spaces/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs. For each user story I created acceptance criteria and tasks, I attached labels for the Epic they belong to and at the beginning of each Iteration I assigned labels with MoSCoW prioritization and story points to each user story assigned to the milestone.

| Link | Notes | Screenshot |
| --- | --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/theresaabl/shared-spaces)](https://www.github.com/theresaabl/shared-spaces/issues) | The open issues contain future features | ![screenshot](documentation/agile/issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/theresaabl/shared-spaces)](https://www.github.com/theresaabl/shared-spaces/issues?q=is%3Aissue+is%3Aclosed) | The closed issues contain all finished Epics, User Stories and Bugs. In the screenshot are a few examples. | ![screenshot](documentation/agile/issues-closed-userstories.png)![screenshot](documentation/agile/issues-closed-bugs.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCow" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

I also used Won't have for future features that were never planned for this release but would be interesting to implement in the future.

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://shared-spaces-f588831ae867.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |
| `HOST` | .herokuapp.com |
| `CSRF_TRUSTED_ORIGIN` | https://*.herokuapp.com |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```

### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary
os.environ.setdefault("HOST", "user-inserts-own-host")
os.environ.setdefault("CSRF_TRUSTED_ORIGIN", "https://localhost")

# local environment only (do not include these in production/deployment!)
# (in settings I made sure that DEBUG = False in heroku if you do not add DEBUG to your config vars there)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/theresaabl/shared-spaces).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/theresaabl/shared-spaces.git`
7. Press "Enter" to create your local clone.


#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/theresaabl/shared-spaces).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [ChatGPT](https://chatgpt.com) | Help with debugging and explanations, also help write the home and about pages text |
| [Stackoverflow](https://stackoverflow.com/a/25797705) | Inspiration on how to set all users to inactive |
| [Stackoverflow](https://stackoverflow.com/a/73085167) | Inspiration on how to set min attribute in calendar to only allow future dates |
| [Saturncloud](https://saturncloud.io/blog/python-pandas-typeerror-unsupported-operand-types-for-datetimetime-and-timedelta/) | Inspiration on how to solve a datetime.time + timedelta typeerror |
| [Stackoverflow](https://stackoverflow.com/a/9579000) | Convert time object to datetime object |
| [Stackoverflow](https://stackoverflow.com/a/46182411) | Inspiration on how to write a custom clean and save method for EventSpaceBooking model |
| [Stackoverflow](https://stackoverflow.com/a/14295709) | Convert string to time object |
| [Stackoverflow](https://stackoverflow.com/a/6076245) | Remove currently tag from image field when editing event space |
| [Stackoverflow](https://stackoverflow.com/a/34614101) | Inspiration on how to get image url |
| [Medium](https://medium.com/@alex.kirkup/integerchoices-in-django-models-working-seamlessly-from-the-backend-and-the-frontend-using-labels-a3e77b86d419) | Display integer choices label in models |
| [mdn web docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/upgrade-insecure-requests) | Convert all insecure requests to secure https ones in base.html |
| [mdn web docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date) | Convert date to 'YYYY-MM-DD' for proper display in date picker |
| [Tim Nelson](https://www.github.com/TravelTimN) and [Stackoverflow](https://stackoverflow.com/a/8125327) | Inspiration to implement onError event when displaying current image in edit event space form |


### Media

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pexels](https://www.pexels.com/photo/aerial-view-of-white-concrete-buildings-during-golden-hours-681368/) | Hero image, sign in image |
| [Pexels](https://www.pexels.com/photo/black-metal-fence-near-person-walking-during-daytime-162024/) | About section header image |
| [Pexels](https://www.pexels.com/photo/two-chairs-with-glass-table-on-living-room-near-window-1571453/) | About section image |
| [Pexels](https://www.pexels.com/photo/two-chairs-with-glass-table-on-living-room-near-window-1571453/) | About section image |
| [Pexels](https://www.pexels.com/photo/a-woman-playing-with-her-daughters-4543704/) | About section image |
| [Pexels](https://www.pexels.com/photo/positive-diverse-people-making-faces-at-camera-3856033/) | About section image |
| [Pexels](https://www.pexels.com/photo/aerial-photo-of-buildings-and-roads-681335/) | Contact page image |
| [Pexels](https://www.pexels.com/photo/water-bottles-on-desks-in-a-conference-room-7648510/) | Event Space Booking image in Resident Space, placeholder image for event spaces |
| [Pexels](https://www.pexels.com/photo/stainless-steel-close-wrench-on-spanner-210881/) | Submit a request image in Resident Space |
| [Pexels](https://www.pexels.com/photo/red-theater-chair-lot-near-white-concrete-pillars-269140/) | Event Spaces Image: Large conference room |
| [Pexels](https://www.pexels.com/photo/people-doing-yoga-in-the-room-8436625/) | Event Spaces Image: Yoga room |
| [Pexels](https://www.pexels.com/photo/family-and-group-of-friends-celebrating-a-child-s-birthday-7180617/) | Event Spaces Image: Large party room |
| [Pexels](https://www.pexels.com/photo/square-beige-wooden-table-with-chairs-260928/) | Event Spaces Image: Small meeting room |
| [Pexels](https://www.pexels.com/photo/sharing-food-3184177/) | Event Spaces Image: Family room |
| [Pexels](https://www.pexels.com/photo/woman-in-blue-denim-jacket-using-macbook-pro-4099099/) | Event Spaces Image: Video call rooms |
| [Pexels](https://www.pexels.com/photo/woman-making-choice-of-dumbbell-4854260/) | Event Spaces Image: Weights room |
| [Pexels](https://www.pexels.com/photo/view-from-broken-brick-wall-into-lake-in-nature-10645596/) | Error 404 image, sign out image, account inactive image, resident space unauthenticated users image |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for ideas on how to fix some issues.
- I would like to thank my family, for believing in me and supporting me, especially in the weeks before the deadline.