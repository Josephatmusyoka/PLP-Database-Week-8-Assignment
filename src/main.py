from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import mysql.connector
from mysql.connector import Error
from typing import List, Optional

# Create FastAPI app instance
app = FastAPI()

# Database connection details
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "1234"
DB_NAME = "inventory_system"

# Function to connect to the MySQL database
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conn.is_connected():
            return conn
    except Error as e:
        raise HTTPException(status_code=500, detail="Database connection error")

# Pydantic models to handle request/response data
class User(BaseModel):
    username: str
    password: str
    role: str
    email: str
    phone: Optional[str] = None

class Supplier(BaseModel):
    name: str
    contact_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    quantity: int
    price: float
    supplier_id: int

class Sale(BaseModel):
    customer_id: int
    item_id: int
    quantity: int
    total_price: float

# Create User
@app.post("/users/", response_model=User)
def create_user(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (username, password, role, email, phone) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (user.username, user.password, user.role, user.email, user.phone))
    conn.commit()
    cursor.close()
    conn.close()
    return user

# Get all Users
@app.get("/users/", response_model=List[User])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Create Supplier
@app.post("/suppliers/", response_model=Supplier)
def create_supplier(supplier: Supplier):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO suppliers (name, contact_name, email, phone, address) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (supplier.name, supplier.contact_name, supplier.email, supplier.phone, supplier.address))
    conn.commit()
    cursor.close()
    conn.close()
    return supplier

# Get all Suppliers
@app.get("/suppliers/", response_model=List[Supplier])
def get_suppliers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM suppliers")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Create Item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO items (name, description, quantity, price, supplier_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (item.name, item.description, item.quantity, item.price, item.supplier_id))
    conn.commit()
    cursor.close()
    conn.close()
    return item

# Get all Items
@app.get("/items/", response_model=List[Item])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Create Sale
@app.post("/sales/", response_model=Sale)
def create_sale(sale: Sale):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO sales (customer_id, item_id, quantity, total_price) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (sale.customer_id, sale.item_id, sale.quantity, sale.total_price))
    conn.commit()
    cursor.close()
    conn.close()
    return sale

# Get all Sales
@app.get("/sales/", response_model=List[Sale])
def get_sales():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sales")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
