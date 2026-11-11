# FastAPI-Notes-API
A beginner-friendly REST API built using Python and FastAPI. This project demonstrates how to create and retrieve notes using HTTP methods, Pydantic validation, and temporary in-memory storage.

Project Overview

The Notes API allows users to:

- Create a new note.
- Store note title and content.
- Retrieve all saved notes.

Tech Stack

- Python – Backend programming language
- FastAPI – Web framework for building APIs
- Pydantic – Data validation
- Uvicorn – ASGI server

Project Structure

fastapi-notes-api/
│
├── main.py
├── requirements.txt
└── README.md

API Endpoints

Method| Endpoint| Description
POST| "/notes"| Create a new note
GET| "/notes"| Retrieve all notes

How It Works

1. User sends note details through an HTTP request.
2. FastAPI receives the request.
3. Pydantic validates the incoming data.
4. Backend creates a note with a unique-looking ID.
5. The note is stored in a Python list.
6. GET API returns all stored notes.

Installation and Setup

1. Clone the repository

git clone YOUR_REPOSITORY_URL

2. Navigate to the project

cd fastapi-notes-api

3. Create a virtual environment

python -m venv venv

4. Activate the environment

Windows:

venv\Scripts\activate

5. Install dependencies

pip install fastapi uvicorn

6. Run the application

uvicorn main:app --reload

7. Open API documentation

http://127.0.0.1:8000/docs

Sample Request

POST /notes

{
  "title": "Python Learning",
  "content": "Learning FastAPI and Backend Development"
}

Sample Response

{
  "message": "Note created successfully",
  "note": {
    "id": 1,
    "title": "Python Learning",
    "content": "Learning FastAPI and Backend Development"
  }
}

Current Limitations

- Uses temporary in-memory storage.
- Notes are lost when the application restarts.
- No user authentication.
- No permanent database integration.

Future Improvements

- Implement UPDATE and DELETE endpoints.
- Integrate PostgreSQL.
- Add user authentication and authorization.
- Implement CRUD operations.
- Add automated API testing using Pytest.

Learning Outcomes

Through this project, I am learning:

- REST API fundamentals.
- HTTP methods (GET and POST).
- FastAPI application structure.
- Pydantic data validation.
- Backend request and response flow.
- Basic API development using Python.
