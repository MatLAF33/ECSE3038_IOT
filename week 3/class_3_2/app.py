#fake database and uvicorn is the server to run the app

from uuid import uuid4, UUID
from fastapi import FastAPI, status, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

class Appiliance(BaseModel): #model for the appliance, it will be used to validate the data that we will receive from the client
    id: UUID = Field(default_factory=uuid4) #it will generate a unique id for each appliance, uuid4 means version 4 of uuid which is random
    name: str
    voltage: int = Field (ge=110, le=240)
    freq: int = Field (ge=50, le=60)
    brand: str
    wattage: int


app = FastAPI()

@app.get("/greetings")
def greetings():
    return "hello world"

@app.get("/greet-person/{name}")
def greet_person(name):
    return f"hello {name}"

@app.get("/adder/{num1}/{num2}")
def adder(num1: int, num2: int):
    ans= num1 + num2
    return {"sum": ans}

items =[
   {
    "id":1,
    "name":"item1"   
   },
   {
    "id":2,
    "name":"item2"
   },
   {
    "id":3,
    "name":"item3"
   }
]

@app.get("/items/{id}")
def get_item_by_id(id: int):
    for item in items:
        if item["id"] == id:
            return item
    return JSONResponse(content={"error": "item not found"}, status_code=status.HTTP_404_NOT_FOUND)

@app.get("/items")
def get_all_items():
    return items

#default path when we run the app, it will show this message
@app.get("/")
def home():
    return "welcome to my api"


#post request to add new item to the list of items, it will receive the data in the form of Appiliance model and add it to the list of itemss
@app.post("/items")
def add_new_item(data: Appiliance):
    new_item=data
    print(new_item)
    itemss.append(new_item)#add to list of itemss below
    return itemss
    #return JSONResponse(content=new_item.model_dump_json(), status_code=status.HTTP_201_CREATED)#

itemss = []

@app.get("/items/this/{item_id}")
def get_item_by_id(item_id: UUID):
    for item in itemss:
        if item.id == item_id: #item.id is from the Appiliance model and item_id is from the path parameter, we are comparing them to find the item with the given id
            return item
    return JSONResponse(content={"error": "item not found"}, status_code=status.HTTP_404_NOT_FOUND)
