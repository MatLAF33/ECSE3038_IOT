from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

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
