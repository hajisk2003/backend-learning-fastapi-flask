# 🚀 Day 5 – Pydantic (FastAPI Backend Learning)

## 📌 Overview

On Day 5 of my FastAPI backend journey, I learned about **data validation and parsing** using Pydantic.
Pydantic is a powerful library used in FastAPI to define request/response schemas and ensure type safety.

---

## 🧠 What I Learned

- ✅ What is Pydantic and why it is used
- ✅ Creating models using `BaseModel`
- ✅ Type validation (int, str, float, etc.)
- ✅ Automatic data parsing
- ✅ Request body validation in FastAPI
- ✅ Error handling for invalid data

---

## 🏗️ Project Structure

```bash
day5-pydantic/
│
├── main.py
├── models.py
└── README.md
```

---

## 💻 Example Code

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/user/")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }
```

---

## ▶️ How to Run

```bash
# Install dependencies
pip install fastapi uvicorn

# Run server
uvicorn main:app --reload
```

---

## 🌐 API Endpoint

- **POST** `/user/`

### Sample Request Body:

```json
{
  "name": "Haji",
  "age": 22,
  "email": "haji@example.com"
}
```

---

## ⚠️ Common Errors Faced

### ❌ Import Error

```
ImportError: cannot import name 'BaseModel' from 'pydantic'
```

### ✅ Fix

- Rename file if named `pydantic.py`
- Delete `__pycache__`

---

## 🎯 Key Takeaways

- Pydantic ensures **data validation automatically**
- FastAPI uses Pydantic for **request/response handling**
- Helps build **robust and error-free APIs**

---

## 🚀 Next Step

➡️ Day 6: Connecting FastAPI with Database (SQL / MongoDB)

---

## 🙌 Author

**Haji Shaikh**
Aspiring Data Scientist | AI/ML Enthusiast | Backend Learner

---
