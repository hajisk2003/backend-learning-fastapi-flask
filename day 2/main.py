from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app=FastAPI()

# model=joblib.load("model.joblib")
#load Pipeline

try:
    model=joblib.load("model.joblib")
except Exception as e:
    print("Error loading model",e)
    model=None


class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    

@app.get("/")
def home():
    return {"message":"ML API is running"}

@app.post("/predict")


def predict(data:InputData):
    
    if model is None:
        raise HTTPException(status_code=500,detail="Model not loaded")
    try:
        
    
        input_array=np.array([[data.feature1, data.feature2, data.feature3]])
    
        prediction=model.predict(input_array)[0]
        return {
            "prediction":float(prediction)
        }
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    