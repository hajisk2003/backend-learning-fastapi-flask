
#data type Validation
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
from typing import List,Dict,Optional,Annotated   
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of the patient in less than 50 chars')]
    # name:str=Field(max_length=50)
    email:EmailStr
    url:AnyUrl 
    age:int
    weight:float=Field(gt=0,lt=120)
    married:bool=False
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('patient must have emergency contact')
        return model
        
    
        
        
        
    

patient_info={'name':'nitish','url':'http://linkdin.com','email':'haji@hdfc.com','age':80,'weight':30.4,'married':False,'contact_details':{'email':'hajisk@gmail.com','Mobile_no':'xxxxxxxxxx','emergency':'92334444'}}
def insert(patient:Patient):
    
    
    
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print("insert into daabae")


patient1=Patient(**patient_info)
insert(patient1)
