
#data type Validation
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated   
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of the patient in less than 50 chars')]
    # name:str=Field(max_length=50)
    email:EmailStr
    url:AnyUrl 
    age:int
    height:float
    weight:float=Field(gt=0,lt=120)
    married:bool=False
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]
    
    
    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/self.height**2)
        return bmi
    
   
        
    
        
        
        
    

patient_info={'name':'nitish','height':5.9,'url':'http://linkdin.com','email':'haji@hdfc.com','age':80,'weight':50,'married':False,'contact_details':{'email':'hajisk@gmail.com','Mobile_no':'xxxxxxxxxx','emergency':'92334444'}}
def insert(patient:Patient):
    
    
    
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print('BMI',patient.calculate_bmi)
    print("insert into daabae")


patient1=Patient(**patient_info)
insert(patient1)
