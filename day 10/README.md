# 🚀 FastAPI + Docker Tutorial (Beginner Friendly)

This project marks **Day 10 (Final Day)** of my journey learning **FastAPI and Python Backend Development**. It demonstrates how to build a simple FastAPI application and Dockerize it for deployment.

---

## 📌 Project Overview

- Build a REST API using FastAPI
- Containerize the application using Docker
- Run the API inside a container
- Learn basic backend deployment concepts

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Docker

---

## 📂 Project Structure

```
.
├── app/
│   ├── main.py
│   └── routes.py (optional)
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚡ FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Docker!"}
```

---

## 📦 Requirements

```
fastapi
uvicorn
```

---

## 🐳 Docker Setup

### Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ▶️ Run Locally

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🐋 Run with Docker

### Build Image

```
docker build -t fastapi-app .
```

### Run Container

```
docker run -d -p 8000:8000 fastapi-app
```

---

## 🌐 Access API

- Swagger UI: http://localhost:8000/docs
- Root: http://localhost:8000/

---

## 🎯 What I Learned

- Building APIs using FastAPI
- Understanding Uvicorn (ASGI server)
- Writing Dockerfiles
- Containerizing backend apps
- Running services in isolated environments

---

## 📈 Future Improvements

- Add database (PostgreSQL / MongoDB)
- Use Docker Compose
- Add JWT Authentication
- Deploy to cloud

---

## 🙌 Acknowledgment

This project is part of my backend learning journey and hands-on practice.
**Hajisab Shaikh**
