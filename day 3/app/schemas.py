from pydantic import BaseModel,Field
class InputData(BaseModel):
    feature1:float=Field(..., gt=0)
    feature2:float=Field(..., gt=0)
    feature3:float=Field(..., gt=0)
    
    
from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def home():
    return {"message":"hello world"}

