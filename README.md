# 🍵 Tea API with FastAPI & Uvicorn

A simple RESTful API using FastAPI that lets you manage a list of teas.

## 🚀 Features

- List all teas
- Add a new tea
- Update existing tea
- Delete a tea

## 🛠 Tech Stack

- FastAPI
- Uvicorn (ASGI server)
- Pydantic (data validation)

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/divanshArora3/tea-api.git
cd tea-api
```
### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the development server
```Bash
uvicorn main:app --reload
```
Visit http://127.0.0.1:8000/docs to explore the Swagger API docs.

## 📬 API Endpoints
| Method | Endpoint         | Description     |
| ------ | ---------------- | --------------- |
| GET    | `/`              | Welcome message |
| GET    | `/teas`          | List all teas   |
| POST   | `/teas`          | Add a new tea   |
| PUT    | `/teas/{tea_id}` | Update a tea    |
| DELETE | `/teas/{tea_id}` | Delete a tea    |
