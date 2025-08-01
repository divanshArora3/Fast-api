from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

# Data Structures
class Tea(BaseModel):
    id: int
    name : str
    origin : str


teas : List[Tea] = []

#Decorator
@app.get("/")
#Function to handle the root path
def read_root():
    return {"message": "Welcome to the Tea API!"}

@app.get("/teas")
def get_teas():
    return teas 

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea
   # return {"message": "Tea added successfully", "tea": tea} 

@app.put("teas/{tea_id}")
def update_tea(tea_id:int ,updated_tea:Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"} 

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
          deleted =  teas.pop(index)
          return deleted
    return {"error": "Tea not found"}