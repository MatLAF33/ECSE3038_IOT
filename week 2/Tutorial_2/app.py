from pyexpat.errors import codes
from pydantic import BaseModel, Field, ValidationError
#Q1) Lookup with a fallback

price_map={}

def print_item_price(price_map, item_name):
    if item_name  in price_map:
        print(f"{item_name} costs {price_map[item_name]}")
    else:
        print(f"{item_name} is not found")

print_item_price({"bread": 280, "milk": 220}, "bread")
print_item_price({"bread": 280, "milk": 220}, "cheese")

#Q2) Update a dict (add or overwrite)

def set_student_score(scores, name, score):
    scores[name] = score
    print(scores)

scores = {"Kai": 64, "Zara": 91}
set_student_score(scores, "Kai", 70)
set_student_score(scores, "Mia", 88)
    
#Q3) Frequency counter
codes=["OK", "OK", "FAIL", "OK", "WARN", "FAIL"]

def count_codes(codes):
    code_freq = {}
    for code in codes:
        if code in code_freq:
            code_freq[code] += 1
        else:
            code_freq[code] = 1

    print(code_freq)

count_codes(codes)

#Q4.1) Create a model
class Reading(BaseModel):
    device_id:str
    temperature:float
    humidity:float
    battery:int =Field(ge=0, le=100)   

#Q4.2) Write a function called: 
def validate_reading(data):
    try:
        reading = Reading(**data)
        print("VALID")
        print(reading)
    except ValidationError as e:
        print("INVALID")
        print(e)

validate_reading({
    "device_id": "esp32-1",
    "temperature": 28.7,
    "humidity": 61.2,
    "battery": 88
})

validate_reading({
    "device_id": "esp32-1",
    "temperature": "hot",
    "humidity": 61.2,
    "battery": 180
})
