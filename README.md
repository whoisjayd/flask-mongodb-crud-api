# Flask MongoDB CRUD API

![visitor badge](https://visitor-badge.laobi.icu/badge?page_id=https://github.com/whoisjayd/flask-mongodb-crud-api)
[![Python Version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://python.org)
[![Flask Version](https://img.shields.io/badge/flask-2.x-blue.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4.4+-green.svg)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/docker-supported-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, ready-to-use RESTful API for user management, built with Flask and MongoDB. This project provides a solid foundation for applications requiring user authentication and data management, with a focus on security and scalability.

## Features

- **Full CRUD Functionality**: Endpoints for creating, reading, updating, and deleting users.
- **Secure by Design**: Passwords are securely hashed using `bcrypt` to protect user data.
- **Centralized Logging**: In-depth logging of application events and errors for easier debugging.
- **Dockerized Environment**: Includes a `Dockerfile` for easy containerization and deployment.
- **Environment-Based Configuration**: Simple setup using environment variables for sensitive data.


## Installation & Setup

### 1. Clone this Repository

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` (`.env.example`) file in the root directory and add:
```ini
MONGO_URI=
SECRET_KEY=
FLASK_ENV="development"
LOG_FILE="logs/app.log"
```

### 4. Run the Flask Application
```sh
python main.py
```
By default, the API runs at `http://localhost:5000/`.



## Docker Support

### 1. Build the Docker Image
```sh
docker build -t flask-app .
```

### 2. Run the Docker Container
```sh
docker run -d -p 5000:5000 --name flask-container flask-app
```

### 3. Stop the Docker Container
```sh
docker stop flask-container
```

### 4. Remove the Docker Container
```sh
docker rm flask-container
```

## API Endpoints

### 1. Get All Users
```http
GET /users
```
**Example:**
```sh
curl -X GET http://localhost:5000/users
```
**Response:**
![get_users](assets/get_users.png)

### 2. Get User by ID
```http
GET /users/{user_id}
```
**Example:**
```sh
curl -X GET http://localhost:5000/users/67b441917c4b7053e07ea45c
```
**Response:**
![get_specific_user](assets/get_specific_user.png)

### 3. Create a New User
```http
POST /users
```
**Request Body:**
```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "password": "secure_password"
}
```
**Response:**
![create_user](assets/create_user.png)

### 4. Update User
```http
PUT /users/{user_id}
```
**Request Body:**
```json
{
  "name": "DoeJohn",
  "email": "joe@example.com",
  "password": "this is my password"
}
```
**Response:**
![user_update](assets/user_update.png)

### 5. Delete User
```http
DELETE /users/{user_id}
```
**Response:**
![delete_user](assets/delete_user.png)



## Proofs
- Data Getting Stored
![mongodb_atlas_db_panel](assets/mongodb_atlas_db_panel.png)
- Working docker container
![img.png](assets/working_docker_container.png)
## Development & Debugging
### Run Flask App
```sh
python main.py
```
### View Logs
Logs are stored in `logs/app.log`. Check them for debugging issues.
