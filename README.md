# Task Manager API (FastAPI)

A lightweight backend service for managing tasks, built with FastAPI.  
Provides a RESTful API with support for CRUD operations, filtering, sorting, and priority-based queries.

---

## Features

- Create, read, update, and delete tasks (CRUD)
- Search tasks by title or description
- Sort tasks by fields (title, status, created_at, priority)
- Retrieve top-N tasks by priority
- Data validation with Pydantic
- Persistent storage using SQLite + SQLAlchemy
- Modular project structure (routers / services / models)

---

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## Project Structure

```
task_manager/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── services.py
│   └── routers/
│       └── tasks.py
├── requirements.txt
└── README.md
```

---

## Installation

1. Clone the repository

```
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

2. Create virtual environment

```
python -m venv venv
source venv/bin/activate  # macOS / Linux
# or
venv\Scripts\activate     # Windows
```

3. Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

```
uvicorn app.main:app --reload
```

API will be available at:

- http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs

---

## API Endpoints

POST /tasks/          - Create task  
GET /tasks/           - Get all tasks (with optional filters)  
GET /tasks/{task_id}  - Get task by ID  
PUT /tasks/{task_id}  - Update task  
DELETE /tasks/{task_id} - Delete task  
GET /tasks/top/{n}    - Get top-N priority tasks  

---

## Example Request

```
{
  "title": "Finish project",
  "description": "Complete FastAPI backend",
  "status": "in_progress",
  "priority": 8
}
```

---

## Possible Improvements

- Add authentication (JWT)
- Use PostgreSQL instead of SQLite
- Add async database support
- Add Docker support
- Add tests
- Add logging and configuration

---

## License

This project is for educational purposes.
