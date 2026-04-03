
#data type Validation
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
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
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper( )
        
        
        
    

patient_info={'name':'nitish','url':'http://linkdin.com','email':'haji@hdfc.com','age':30,'weight':30.4,'married':False,'contact_details':{'email':'hajisk@gmail.com','Mobile_no':'xxxxxxxxxx'}}
def insert(patient:Patient):
    
    
    
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print("insert into daabae")


patient1=Patient(**patient_info)
insert(patient1)
