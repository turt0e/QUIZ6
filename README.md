# User Post Management Platform

This project is a platform where users can register, post content, and manage their posts. Each user is allowed to post only once, and admin approval is required for newly registered users to log in.

## Features

1. **User Authentication**
   - Login using Email, Username, or Contact Number.
   - User model includes:
     - Email
     - Username
     - Contact Number

2. **Post Management**
   - Users can create a post with the following attributes:
     - User
     - Content
     - Created At (timestamp)

3. **User Registration**
   - Registration form collects:
     - Email
     - Username
     - Contact Number
     - Password
     - Confirm Password
   - Newly registered users cannot log in until an admin approves their account.

4. **Action Feedback**
   - Display proper messages after actions (e.g., "Post created successfully", "Account successfully created").

5. **Report Functionality**
   - Users can report posts or other users, with an input message for the report.

6. **Post List View**
   - Displays a paginated list of posts (3 posts per page).
   - Content is truncated if longer than 100 characters, with an option to "see more".
   - Shows username in the format: `username > us***me`.
   - Post creation date formatted as YYYY-MM-DD.

7. **Admin Dashboard**
   - Admins can approve user registrations, manage posts, and view reports.
   - Paginated view for admin management (5 objects per page).

8. **Responsive Design**
   - Utilizes Bootstrap for responsiveness on both desktop and mobile devices.

9. **Dark Mode Option**
   - Users can toggle dark mode, with a separate model to store their preference.

10. **Requirements**
    - Includes a `requirements.txt` for necessary packages.
