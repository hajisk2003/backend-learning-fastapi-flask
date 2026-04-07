from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field,field_validator
from typing import Literal, Annotated
import pickle
import pandas as pd
from schema.user_input import UserInput
from model.predict import predict_output,model,MODEL_VERSION
from schema.prediction_response import PredictionResponse



    
#MLflow
MODEL_VERSION='1.0.0'

app = FastAPI()



    
@app.get('/')
def home():
    return {'message':"welcome to model"}

@app.get('/health')
def health_check():
    return {
        'status':'ok',
        'version':MODEL_VERSION
    }
    

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    try:
        

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
        
        




