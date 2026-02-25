from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app=FastAPI()

model=joblib.load("model.joblib")

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    

@app.get("/")
def home():
    return {"message":"ML API is running"}

@app.post("/predict")
def predict(data:InputData):
    input_array=np.array([[data.feature1, data.feature2, data.feature3]])
    
    prediction=model.predict(input_array)[0]
    return {
        "prediction":float(prediction)
    }
    
    