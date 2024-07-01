# Flask User Management Application

This is a simple Flask application that allows for user registration, login, and updating user details. The application uses an in-memory list to store user information and displays flash messages for user feedback.

## Features

- User registration with name, email, and password.
- User login with email and password.
- Update user details (name and password).
- Flash messages for user feedback.
- Session management for logged-in users.

## Requirements

- Python 3.6+
- Flask
- Werkzeug
- Flask-Session

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/flask-user-management.git
    cd flask-user-management
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```sh
    pip install Flask Werkzeug Flask-Session
    ```

## Usage

1. Run the Flask application:

    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

```plaintext
flask-user-management/
│
├── app.py
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── registration.html
│   └── update.html
└── static/
    └── css/
        └── login_page.css
```

## Routes
- / - Home page
- /login - User login
- /registration - User registration
- /update - Update user details

## Templates
- home.html - The home page template.
- login.html - The login page template.
- registration.html - The registration page template.
- update.html - The update details page template.

