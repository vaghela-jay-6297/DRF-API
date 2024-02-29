1. User Registration:
- Implement a REST API endpoint for user registration.
- Include fields such as username, email, password.
- Validate input data and handle registration errors appropriately.
2. User Login:
- Create a REST API endpoint for user login.
- Use token-based authentication (JWT) for secure authentication.
- Return a JWT token upon successful login.
3. Profile Update:
- Develop a REST API endpoint for users to update their profiles.
- Allow users to modify information like username, email, and other relevant details.
- Ensure that only authenticated users can update their profiles.
4. Forgot Password with Email:
- Implement a REST API endpoint for users to initiate a password reset via email.
- Send a unique reset link to the user's registered email address.
- Include a time-limited validity period for the reset link.
- Create a secure mechanism for updating the password.
5. Admin Panel:
- Develop an admin panel using Bootstrap for the user interface.
- Include a page where administrators can view a list of all registered users.
- Display relevant user details (e.g., username, email) in a tabular format.
6. Database:
- Use Django ORM to define models for user data.
- Set up database migrations to create necessary tables.
- Use a relational database (PostgreSQL).
7. Submission:
- Provide a link to your GitHub repository containing the Django application source code.
- Include the database schema or migration files.
- Share a Postman collection containing sample requests for each API endpoint.