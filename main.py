from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = {}

class Item(BaseModel):
    name: str
    price: float
 
    


@app.post("/create_item/")
def create_item(item: Item):
    db[item.name] = item.price
    return item

@app.get("/items/{item_name}")
def read_item(item_name: str):
    return db[item_name]

@app.get("/items/")
def read_items():
    return db

@app.delete("/items/{item_name}")
def delete_item(item_name: str):
    del db[item_name]

@app.put("/items/{item_name}")
def update_item(item_name: str, item: Item):
    db[item_name] = item.price
    return item

