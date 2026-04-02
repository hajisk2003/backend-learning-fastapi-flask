
#data type Validation
from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List,Dict,Optional   
class Patient(BaseModel):
    name:str
    email:EmailStr
    url:AnyUrl
    age:int
    weight:float
    married:bool=False
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]
    

patient_info={'name':'nitish','url':'http://linkdin.com','email':'haji@gmail.com','age':30,'weight':30.4,'married':False,'contact_details':{'email':'hajisk@gmail.com','Mobile_no':'xxxxxxxxxx'}}
def insert(patient:Patient):
    
    
    
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print("insert into daabae")


patient1=Patient(**patient_info)
insert(patient1)

# def insert(name :str,age: int):
#     if type(name)==str and type(age)==int:
#         print(name)
#         print(age)
    
#     # print(name)
#     # print(age)
#     print("insert into daabae")
    
# insert('haji','thirty')
