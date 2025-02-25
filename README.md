# [SharedSpaces](https://shared-spaces-f588831ae867.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/TheresaAbl/shared-spaces)](https://www.github.com/TheresaAbl/shared-spaces/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/TheresaAbl/shared-spaces)](https://www.github.com/TheresaAbl/shared-spaces/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheresaAbl/shared-spaces)](https://www.github.com/TheresaAbl/shared-spaces)

A website for a community living space called SharedSpaces. 

Live Site - [SharedSpaces](https://shared-spaces-f588831ae867.herokuapp.com/)

![screenshot](documentation/mockup.png)

source: [shared-spaces amiresponsive](https://ui.dev/amiresponsive?url=https://shared-spaces-f588831ae867.herokuapp.com)

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "I Think Therefore I Blog".

## UX

### The 5 Planes of UX

#### 1. Strategy Plane
##### Purpose
- Provide blog owners with tools to create, manage, and moderate engaging blog content and user interactions.
- Offer users and guests an intuitive platform to explore, engage, and contribute to blog discussions.

##### Primary User Needs
- Blog owners need seamless tools for publishing and managing posts and comments.
- Registered users need the ability to engage with blog content through comments and account features.
- Guests need the ability to browse and enjoy blog content without registration.

##### Business Goals
- Foster a dynamic blogging platform with active user participation.
- Build a sense of community through discussions and user engagement.
- Ensure easy blog content management for owners.

#### 2. Scope Plane
##### Features
- A full list of [Features](#features) can be viewed in detail below.

##### Content Requirements
- Blog post management (create, update, delete, and preview).
- Comment moderation and management tools.
- User account features (register, log in, edit/delete comments).
- Notification system for comment approval status.
- 404 error page for lost users.

#### 3. Structure Plane
##### Information Architecture
- **Navigation Menu**:
  - Links to Home, Blog Posts, Login/Register, and Dashboard (for blog owners).
- **Hierarchy**:
  - Blog content displayed prominently for easy browsing.
  - Clear call-to-action buttons for account creation and engagement (e.g., commenting).

##### User Flow
1. Guest users browse blog content → read posts and see commenter names.
2. Guest users register for an account → log in to leave comments.
3. Registered users leave comments → receive a pending approval notification.
4. Blog owners create, update, and manage posts → moderate comments.
5. Blog owners approve or reject comments → manage user interactions.

#### 4. Skeleton Plane
##### Wireframe Suggestions
- A full list of [Wireframes](#wireframes) can be viewed in detail below.

#### 5. Surface Plane
##### Visual Design Elements
- **[Colours](#colour-scheme)**: see below.
- **[Typography](#typography)**: see below.

### Colour Scheme

I used [coolors.co](https://coolors.co/324495-f6ae2d-f26419-ffffff-212529) to generate my color palette. The goal was a very clean and simple, but still vibrant and inviting look. I used shades of yellow, orange and blue to style the highlights throughout the site (e.g. headings, borders, buttons etc.) which gives a bright and vibrant look, the rest is kept very simple with white background and dark-grey text, where the dark grey is the standard bootstrap body text color.


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


![screenshot](documentation/coolors.png)

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

⚠️ INSTRUCTIONS ⚠️

In this section, you should go over the different parts of your project, and describe each feature. You should explain what value each of the features provides for the user, focusing on your target audience, what they want to achieve, and how your project can help them achieve these things.

**IMPORTANT**: Remember to always include a screenshot of each individual feature!

⚠️ --- END --- ⚠️

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Blog List | The homepage displays basic information about blog posts, including image, title, author, date, and a brief excerpt. | ![screenshot](documentation/features/blog-list.png) |
| View Post | Users can view the full blog post details, including any comments. | ![screenshot](documentation/features/view-post.png) |
| Pagination | Blog posts are displayed in pages, with six posts per page. This provides better navigation for users through the post list. | ![screenshot](documentation/features/pagination.png) |
| Add Comments | Authenticated visitors can comment on blog posts; comments require approval before being published. | ![screenshot](documentation/features/add-comment.png) |
| Edit Comments | Authenticated visitors can edit their own comments. | ![screenshot](documentation/features/edit-comment.png) |
| Delete Comments | Authenticated visitors can delete their own comments. | ![screenshot](documentation/features/delete-comment.png) |
| Comment Approvals | Admins can approve or disapprove comments submitted by users before they are visible on the blog post. | ![screenshot](documentation/features/comment-approval.png) |
| Create Post | Site owners can create/publish blog posts, including setting a featured image using Cloudinary, all from the Django admin dashboard. | ![screenshot](documentation/features/create-post.png) |
| Update Post | Site owners can update/manage blog posts from the Django admin dashboard. | ![screenshot](documentation/features/update-post.png) |
| Delete Post | Site owners can delete blog posts from the Django admin dashboard. | ![screenshot](documentation/features/delete-post.png) |
| About Page | The About page displays the latest information about the site author, along with the option for visitors to send collaboration requests. | ![screenshot](documentation/features/about.png) |
| Collaboration Requests | Visitors can submit collaboration requests from the *About* page, which are later reviewed by the admin. | ![screenshot](documentation/features/collaboration.png) |
| User Feedback | Clear and obvious Django messages are used to provide feedback to user actions. | ![screenshot](documentation/features/messages.png) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/features/heroku.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

### Future Features

⚠️ INSTRUCTIONS ⚠️

Do you have additional ideas that you'd like to include on your project in the future? Fantastic, list them here! It's always great to have plans for future improvements. Consider adding any helpful links or notes to help remind you in the future, if you revisit the project in a couple years.

A few examples are listed below to align with possible ways to improve on the sample walkthrough project, to give you some inspiration.

⚠️ --- END ---⚠️

- **Post Categories/Tags**: Allow users to categorize and tag blog posts, making it easier for visitors to filter content based on their interests.
- **Post Search Functionality**: Add a search bar for users to quickly find posts by keywords or phrases.
- **Post Likes/Dislikes or Upvotes**: Implement a "like" or "upvote" system for blog posts to encourage user engagement and give feedback to the author.
- **User Profiles**: Create personalized user profiles where authenticated users can view their comments, liked posts, and account information.
- **Comment Replies & Threads**: Enable users to reply to comments, creating nested comment threads for better discussions.
- **Post Sharing**: Add social media sharing buttons (e.g., Twitter, Facebook, LinkedIn) for users to share blog posts.
- **Notifications**: Implement a notification system that alerts users when their comments are approved, when new comments are made on a post they've commented on, or when new posts are published.
- **Email Subscriptions**: Allow users to subscribe to receive email notifications for new posts, updates, or newsletters.
- **Post Analytics**: Provide post authors with analytics such as views, time spent reading, and engagement rates.
- **Multilingual Support**: Add the ability to write and view blog posts in multiple languages, broadening the audience.
- **Related Posts Recommendations**: Show related posts at the bottom of a blog post to encourage further reading and keep users engaged.
- **Content Flagging/Reporting**: Allow users to flag or report inappropriate content (comments or posts) for moderation.
- **SEO Optimization**: Implement features for SEO, such as meta tags, custom URLs, and keywords for better search engine ranking.
- **User Dashboard**: Provide users with a dashboard to track their activity, such as comments made, likes received, and blog posts they’ve interacted with.
- **Admin Dashboard Analytics**: Provide site admins with an analytics dashboard showing user activity, popular posts, most commented articles, etc.
- **Custom Themes for Users**: Allow users to customize the visual theme of the site (colors, fonts, etc.) to suit their preferences.

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
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |

⚠️ NOTE ⚠️

Want to add more?

- Tutorial: https://shields.io/badges/static-badge
- Icons/Logos: https://simpleicons.org
  - FYI: not all logos are available to use

🛑 --- END --- 🛑

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

🛑 !!! ATTENTION TheresaAbl !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️

🛑 --- END --- 🛑

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

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

🛑 !!! ATTENTION TheresaAbl !!! 🛑

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️

🛑 --- END --- 🛑

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
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

1. Go to the [GitHub repository](https://www.github.com/TheresaAbl/shared-spaces).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/TheresaAbl/shared-spaces.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/TheresaAbl/shared-spaces)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/TheresaAbl/shared-spaces).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss any differences between the local version you've developed, and the live deployment site. Generally, there shouldn't be [m]any major differences, so if you honestly cannot find any differences, feel free to use the following example:

⚠️ --- END --- ⚠️

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

⚠️ INSTRUCTIONS ⚠️

In the following sections, you need to reference where you got your content, media, and any extra help. It is common practice to use code from other repositories and tutorials (which is totally acceptable), however, it is important to be very specific about these sources to avoid potential plagiarism.

⚠️ --- END ---⚠️

### Content

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links for any borrowed code snippets, elements, and resources. Ideally, you should provide an actual link to every resource used, not just a generic link to the main site. If you've used multiple components from the same source (such as Bootstrap), then you only need to list it once, but if it's multiple Codepen samples, then you should list each example individually. If you've used AI for some assistance (such as ChatGPT or Perplexity), be sure to mention that as well. A few examples have been provided below to give you some ideas.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution links to any media files borrowed from elsewhere (images, videos, audio, etc.). If you're the owner (or a close acquaintance) of some/all media files, then make sure to specify this information. Let the assessors know that you have explicit rights to use the media files within your project. Ideally, you should provide an actual link to every media file used, not just a generic link to the main site, unless it's AI-generated artwork.

Looking for some media files? Here are some popular sites to use. The list of examples below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links by sending yourself (or Slackbot) the following command: `!freemedia`.

- Images
    - [Pexels](https://www.pexels.com)
    - [Unsplash](https://unsplash.com)
    - [Pixabay](https://pixabay.com)
    - [Lorem Picsum](https://picsum.photos) (placeholder images)
    - [Wallhere](https://wallhere.com) (wallpaper / backgrounds)
    - [This Person Does Not Exist](https://thispersondoesnotexist.com) (reload to get a new person)
- Audio
    - [Audio Micro](https://www.audiomicro.com/free-sound-effects)
- Video
    - [Videvo](https://www.videvo.net)
- Image Compression
    - [TinyPNG](https://tinypng.com) (for images <5MB)
    - [CompressPNG](https://compresspng.com) (for images >5MB)

A few examples have been provided below to give you some ideas on how to do your own Media credits.

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [I Think Therefore I Blog](https://codeinstitute.net) | Sample images provided from the walkthrough projects |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pexels](https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg) | Hero image |
| [Wallhere](https://c.wallhere.com/images/9c/c8/da4b4009f070c8e1dfee43d25f99-2318808.jpg!d) | Background wallpaper |
| [Pixabay](https://cdn.pixabay.com/photo/2017/09/04/16/58/passport-2714675_1280.jpg) | Background wallpaper |
| [DALL-E 3](https://openai.com/index/dall-e-3) | AI generated artwork |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

⚠️ INSTRUCTIONS ⚠️

Use this space to provide attribution and acknowledgement to any supports that helped, encouraged, or supported you throughout the development stages of this project. It's always lovely to appreciate those that help us grow and improve our developer skills. A few examples have been provided below to give you some ideas.

⚠️ --- END ---⚠️

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.

