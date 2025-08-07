from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the data structure
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# GET endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# POST endpoint to calculate an item cost
@app.post("/cart/")
def create_cart(item: Item):
    tax_total = item.price * item.tax
    total = item.price + tax_total
    return {'total': total}