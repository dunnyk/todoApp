Todo App
Overview
This Todo App is a simple task management application built with Flask and SQLAlchemy. It allows users to create, manage, and track tasks efficiently.

Features
User Authentication: Secure user registration and login using token-based authentication.
Task Management: Create, update, delete, and view tasks.
Tagging System: Assign tags to tasks for better organization.
RESTful API: Built using Flask-RESTx for easy integration and extension.
Project Structure
app/: Contains the main application modules.
models.py: Defines the User, Task, Tag, and TaskTag models.
routes/: Contains the Blueprint and API route definitions.
schemas/: Marshmallow schemas for data validation and serialization.
migrations/: Alembic migrations for database version control.
config.py: Configuration settings for different environments.
Installation
Clone the repository:

bash
Copy code
git remote add origin https://github.com/dunnyk/todoApp.git
Set up a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the environment variables:

Create a .env file in the root directory and add the necessary environment variables (e.g., DATABASE_URL, SECRET_KEY).
Initialize the database:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Run the application:

bash
Copy code
flask run
Usage
API Endpoints:
POST /register: Register a new user.
POST /login: Log in and obtain an authentication token.
POST /tasks: Create a new task.
GET /tasks: Retrieve all tasks.
PUT /tasks/<task_id>: Update a task.
DELETE /tasks/<task_id>: Delete a task.
