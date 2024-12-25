from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import Response
import csv
import os
from typing import List
from functools import lru_cache

# Define the data models
class User(BaseModel):
    id: int
    name: str
    email: str

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# File paths
USER_CSV = "users.csv"
PRODUCT_CSV = "products.csv"

# Helper functions to read/write CSV files
def read_csv(file_path, model):
    data = []
    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(model(**{key: int(value) if value.isdigit() else value for key, value in row.items()}))
    return data

def write_csv(file_path, data, fieldnames):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows([item.dict() for item in data])

# Cache helper function
@lru_cache()
def get_users():
    return read_csv(USER_CSV, User)

@lru_cache()
def get_products():
    return read_csv(PRODUCT_CSV, Product)

# Endpoints for Users
@app.get("/users", response_model=List[User])
def list_users():
    return get_users()
@app.get("/users/{user_id}", response_model=User)
def get_user_with_id(user_id: int):
    users = get_users()
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found.")


@app.post("/users", response_model=User, status_code=201)
def add_user(user: User):
    users = get_users()
    if any(u.id == user.id for u in users):
        raise HTTPException(status_code=400, detail="User ID already exists.")
    users.append(user)
    write_csv(USER_CSV, users, fieldnames=User.__fields__.keys())
    return user
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, name: str, email: str):
    users = get_users()
    for user in users:
        if user.id == user_id:
            user.name = name
            user.email = email
            write_csv(USER_CSV, users, fieldnames=User.__fields__.keys())
            return user
    raise HTTPException(status_code=404, detail="User not found.")


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    users = get_users()
    for user in users:
        if user.id == user_id:
            users.remove(user)
            write_csv(USER_CSV, users, fieldnames=User.__fields__.keys())
            return Response(status_code=204)  
    raise HTTPException(status_code=404, detail="User not found.")

# Endpoints for Products
@app.get("/products", response_model=List[Product])
def list_products():
    return get_products()
@app.get("/products/{product_id}", response_model=Product)
def get_product_with_id(product_id: int):
    products = get_products()
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found.")

@app.post("/products", response_model=Product, status_code=201)
def add_product(product: Product):
    products = get_products()
    if any(p.id == product.id for p in products):
        raise HTTPException(status_code=400, detail="Product ID already exists.")
    products.append(product)
    write_csv(PRODUCT_CSV, products, fieldnames=Product.__fields__.keys())
    return product

@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    products = get_products()
    for product in products:
        if product.id == product_id:
            products.remove(product)
            write_csv(PRODUCT_CSV, products, fieldnames=Product.__fields__.keys())
            return Response(status_code=204)  
    raise HTTPException(status_code=404, detail="Product not found.")

# Endpoint to update stock
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, new_price: int, stock: int):
    products = get_products()
    for product in products:
        if product.id == product_id:
            product.stock = stock
            product.price= new_price
            write_csv(PRODUCT_CSV, products, fieldnames=Product.__fields__.keys())
            return product
    raise HTTPException(status_code=404, detail="Product not found.")

# Add Cache-Control header to responses
@app.middleware("http")
async def add_cache_header(request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "public, max-age=60"
    return response
