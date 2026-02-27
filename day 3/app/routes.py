from fastapi import APIRouter,HTTPException
import numpy as np
from app.schemas import InputData
from app.model_loader import load_model
from app.logger import log_info,log_error

router=APIRouter()
model=load_model()

@router.get("/")
def home():
    return {"message":"structure ML API"}

@router.post("/predict")
def predict(data:InputData):
    if model is None:
        log_error("model not loaded")
        raise HTTPException(status_code=500,detail="model not loaded")
    try:
        input_array=np.array([[data.feature1,data.feature2,data.feature3]])
        prediction=model.predict(input_array)[0]
        log_info(f"prediction made:{prediction}")
        return {"prediction":float(prediction)}
    except Exception as e:
        log_error(str(e))
        raise HTTPException(status_code=400,detail=str(e))