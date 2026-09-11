Flask C10 Summative Lab — Sessions and JWT Clients

Project Overview

This project demonstrates authentication and authorization using a Flask backend with two separate client applications.

The project includes:

- A Flask API server
- Session-based authentication client
- JWT-based authentication client
- Flask-SQLAlchemy database integration
- Flask-Migrate database migrations
- Protected API routes
- User authentication and authorization

Project Structure

flask-c10-summative-lab-sessions-and-jwt-clients/
│
├── client-with-jwt/          # Client application using JWT authentication
├── client-with-sessions/     # Client application using session authentication
├── migrations/               # Flask-Migrate database migrations
├── server/                   # Flask backend API
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   └── seed.py
│
├── .env                      # Environment variables
├── .gitignore
├── requirements.txt          # Python dependencies
└── README.md

Technologies Used

Backend

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy
- JWT authentication
- Session authentication

Clients

- JavaScript
- Node.js
- npm
- React/client-side authentication

Installation

Clone the repository and enter the project directory:

git clone <repository-url>
cd flask-c10-summative-lab-sessions-and-jwt-clients

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install the Python dependencies:

pip install -r requirements.txt

Environment Variables

Create a ".env" file in the project root and configure the required environment variables for the Flask application.

Do not commit passwords, secret keys, tokens, or other sensitive information to GitHub.

Running the Flask Server

From the project root, activate the virtual environment:

source venv/bin/activate

Then start the Flask application using the configuration required by the project.

The backend API will then be available locally.

Database

The project uses SQLAlchemy and Flask-Migrate for database management.

To initialize or update the database, use the Flask-Migrate commands configured for the project.

For example:

flask db upgrade

The seed script can be used to populate the database with sample data:

python server/seed.py

Client Applications

JWT Client

The "client-with-jwt" directory contains the client application that communicates with the Flask API using JSON Web Tokens for authentication.

Navigate into the directory and install its dependencies:

cd client-with-jwt
npm install

Start the client using the appropriate npm command defined in "package.json".

Sessions Client

The "client-with-sessions" directory contains the client application that uses Flask session-based authentication.

Navigate into the directory and install its dependencies:

cd client-with-sessions
npm install

Start the client using the appropriate npm command defined in "package.json".

Authentication

This project demonstrates two authentication approaches:

Session Authentication

The server maintains authentication state using sessions. After successful login, the client can make authenticated requests while the session remains valid.

JWT Authentication

The server issues a JSON Web Token after successful authentication. The client uses the token when making requests to protected API endpoints.

Testing

Run the project's tests using:

pytest

Make sure the virtual environment is activated and all dependencies are installed before running the tests.

Git Collaboration

This project was developed collaboratively using Git branches.

Each team member worked on their assigned features using their own branch. Completed work was merged into the main branch before submission.

The "main" branch contains the combined project implementation.

Contributors

- Terry Mpaera
- Project team members

License

This project was created as part of a Moringa School software development course assignment.