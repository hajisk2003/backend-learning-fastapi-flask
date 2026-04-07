# 🚀 Serving ML Models with FastAPI

## 📌 Overview

This project demonstrates how to **deploy and serve Machine Learning models as APIs** using FastAPI.
It enables real-time predictions by exposing trained ML models through RESTful endpoints.

---

## 🎯 Objectives

- Build a scalable backend for ML model inference
- Expose models via REST APIs
- Handle request validation using Pydantic
- Enable fast and efficient model serving

---

## 🧠 Key Concepts Covered

- ✅ Model serialization (Pickle / Joblib)
- ✅ API development with FastAPI
- ✅ Request & response validation using Pydantic
- ✅ Real-time inference
- ✅ Error handling and input validation
- ✅ API testing using Swagger UI

---

## 🏗️ Project Structure

```bash
ml-fastapi/
│
├── model/
│     └── model.pkl
│
├── app/
│     ├── main.py
│     ├── schema.py
│     └── utils.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/your-username/ml-fastapi.git

# Navigate to project
cd ml-fastapi

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

👉 Server runs at:

```
http://127.0.0.1:8000
```

---

## 🌐 API Endpoints

### 🔹 Health Check

```
GET /
```

### 🔹 Predict Endpoint

```
POST /predict
```

---

## 📥 Sample Request

```json
{
  "feature1": 10,
  "feature2": 20,
  "feature3": 30
}
```

---

## 📤 Sample Response

```json
{
  "prediction": 1
}
```

---

## 💻 Example Code

```python
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Load model
model = pickle.load(open("model/model.pkl", "rb"))

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(data: InputData):
    input_values = [[data.feature1, data.feature2, data.feature3]]
    prediction = model.predict(input_values)
    return {"prediction": int(prediction[0])}
```

---

## 🧪 Testing

👉 Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

Test API directly from browser.

---

## ⚠️ Common Issues

### ❌ Model not loading

- Check file path
- Ensure correct serialization format

### ❌ Validation error

- Ensure input matches Pydantic schema

---

## 🚀 Future Enhancements

- ✅ Docker containerization
- ✅ CI/CD pipeline
- ✅ Authentication (JWT)
- ✅ Deploy on cloud (AWS / GCP / Render)
- ✅ Batch prediction support

---

## 🧠 Key Takeaways

- FastAPI provides **high-performance API serving**
- Pydantic ensures **data validation**
- Easy integration with ML models for production-ready systems

---

## 🙌 Author

**Haji Shaikh**
AI/ML Enthusiast | Data Science Student | Backend Developer

---

## ⭐ Support

If you found this helpful, please ⭐ the repository!

---
