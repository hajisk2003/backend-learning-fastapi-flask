from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int

def insert_data(patient:Patient):
     print(patient.name)
     print(patient.age)
     print('inserrted')
     
Patient_info={'name':'haji','age':30}
patient1=Patient(**Patient_info)
insert_data(patient1)