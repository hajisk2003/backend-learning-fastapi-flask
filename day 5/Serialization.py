from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str
    

class Patient(BaseModel):
    name:str
    gender:str
    age:int 
    address:Address
    
    
address_dict={'city':'Pune','state':'Maharshtra','pin':'411018'}
address1=Address(**address_dict)

patient_dict={'name':'nitish','gender':'Male','age':32,'address':address1}

patient1=Patient(**patient_dict)

# print(patient1)
# print(patient1.address)

# temp=patient1.model_dump()
# temp=patient1.model_dump_json()
temp=patient1.model_dump(include=['name'])
temp=patient1.model_dump(exclude=['name'])

print(temp)
print(type(temp))