# 🚀 Day 6 – FastAPI: POST Request & Add Data

Today, I focused on implementing POST APIs in FastAPI to create and store new data. I built a Patient Management System API where users can add patient records dynamically.

---

## 📌 Topics Covered

- Understanding POST requests in REST APIs
- Creating API endpoints using FastAPI
- Using Pydantic models for request validation
- Adding new data to a JSON file (acting as a database)
- Handling duplicate entries with proper error responses
- Returning custom HTTP responses

---

## 🛠️ Implementation Details

### ✅ 1. Pydantic Model

Used Pydantic to validate incoming request data:

```python
class Patient(BaseModel):
    id: str
    name: str
    city: str
    age: int
    gender: str
    height: float
    weight: float
```

---

### ✅ 2. POST API to Create Patient

```python
@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    data[patient.id] = patient.model_dump(exclude=['id'])
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'patient created successfully'})
```

---

### ✅ 3. JSON File as Database

- Used `patients.json` to store records
- Implemented:
  - `load_data()` → read data
  - `save_data()` → write data

---

## 🧪 Example Request

### 📥 POST `/create`

```json
{
  "id": "P001",
  "name": "John",
  "city": "Pune",
  "age": 25,
  "gender": "male",
  "height": 1.75,
  "weight": 70
}
```

---

## 📤 Response

```json
{
  "message": "patient created successfully"
}
```

---

## ⚠️ Error Handling

- Duplicate ID → returns 400 error
- Invalid data → automatically handled by Pydantic
- Empty JSON file → handled using try-except

---

## 📚 Learning Outcome

- Learned how to create POST APIs in FastAPI
- Understood request validation using Pydantic
- Gained hands-on experience in handling real-world backend logic
- Improved understanding of API design and error handling

---

## 🚀 Next Goals

- Implement PUT (Update API)
- Implement DELETE API
- Connect with a real database (MySQL/PostgreSQL)
- Add authentication (JWT)

---

## 👨‍💻 Author

Shaikh Hajisab
Aspiring Backend Developer | AI & ML Enthusiast

---
