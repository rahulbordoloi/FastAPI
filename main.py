# Importing the Libraries
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Creating a FastAPI Instance
app = FastAPI()

# CLass to define the arguments for API
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


# Asynchronous Default Route
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Asynchronous Route for 'localhost:port_no/items/{item_id} [PUT Request]
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# Asynchronous Route for 'localhost:port_no/items/{item_id} [GET Request]
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

