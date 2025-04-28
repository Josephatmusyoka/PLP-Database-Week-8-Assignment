
# Inventory Management System

## Project Description

This project is a **Full-Stack Inventory Management System** built using **FastAPI** (Python) for the backend and **MySQL** for the database. The system is designed to manage various aspects of an inventory, including users, suppliers, items, and sales. The project implements CRUD (Create, Read, Update, Delete) operations for these resources through a RESTful API.

### Key Features:
- **User Management**: Admin can create, read, update, and delete users.
- **Supplier Management**: Manage supplier details and link suppliers to inventory items.
- **Inventory Management**: Keep track of items (e.g., stock levels, prices).
- **Sales Management**: Record and track sales transactions.

This system is ideal for small to medium-sized businesses that need an efficient way to manage their inventory and sales.

---

## Features

- **CRUD operations for Users, Suppliers, Items, and Sales**
- **Database connection to MySQL**
- **FastAPI-based RESTful API for managing resources**
- **MySQL schema and sample data insertion scripts**
- **Complete setup with Docker support (optional)**

---

## Setup Instructions

### Prerequisites

Before running the project, you need to have the following installed on your machine:

- **Python** 3.8+ (for the backend)
- **MySQL** (for the database)
- **pip** (for managing Python dependencies)

---

### Step 1: Set Up MySQL

1. **Create a Database**:

   First, create a new MySQL database called `inventory_system`. You can do this using the following command in MySQL:

   ```sql
   CREATE DATABASE inventory_system;
   ```

2. **Import Database Schema**:

   Import the schema to set up the required tables. You can use the `inventory_management.sql` file to create the tables:

   ```bash
   mysql -u root -p inventory_system < src/inventory_management.sql
   ```

3. **Insert Sample Data**:

   After creating the tables, you can insert sample data using the `insert_sample_data.sql` file. This will populate your database with sample records for users, suppliers, items, and sales:

   ```bash
   mysql -u root -p inventory_system < src/insert_sample_data.sql
   ```

---

### Step 2: Install Dependencies

Install the required Python dependencies by running the following command:

```bash
pip install -r src/requirements.txt
```

This will install **FastAPI**, **Uvicorn**, **MySQL connector**, and **Pydantic**.

---

### Step 3: Running the FastAPI Application

Once all dependencies are installed, you can run the FastAPI application using **Uvicorn**:

```bash
uvicorn src.main:app --reload
```

This will start the FastAPI server, and you can access the API on `http://127.0.0.1:8000`.

---

### Step 4: Testing the API

The application exposes several RESTful endpoints to interact with the inventory system. You can test the API by using tools like **Postman**, **Curl**, or the browser for GET requests. The available endpoints are:

- `POST /users/`: Create a new user
- `GET /users/`: Retrieve all users
- `POST /suppliers/`: Create a new supplier
- `GET /suppliers/`: Retrieve all suppliers
- `POST /items/`: Create a new item
- `GET /items/`: Retrieve all items
- `POST /sales/`: Create a new sale
- `GET /sales/`: Retrieve all sales

---

## API Documentation

FastAPI automatically generates interactive API documentation that you can view in your browser at the following URL:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

---

## Optional: Docker Setup

You can also run this application using Docker. Below are the steps to set up Docker.

1. **Create a Docker Image**:

   To build the Docker image for the FastAPI application, run the following command:

   ```bash
   docker build -t inventory-system .
   ```

2. **Run the Docker Container**:

   After the image is built, you can run the Docker container using:

   ```bash
   docker run -d -p 8000:8000 --name inventory-system inventory-system
   ```

   This will start the application in a Docker container, and you can access it on `http://127.0.0.1:8000`.

---

## Contributing

1. Fork the repository.
2. Clone your forked repository:
   ```bash
   git clone https://github.com/Josephatmusyoka/PLP-Database-Week-8-Assignment.git
   ```
3. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
5. Push your changes to your fork:
   ```bash
   git push origin feature-name
   ```
6. Open a Pull Request to merge your changes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions, feel free to reach out:

- Email: `Josephatmusyoka715@gmail.com`
- GitHub: (https://github.com/Josephatmusyoka)

---

### **ERD (Entity Relationship Diagram)**

Below is a link to the **ERD** for this project:

- [ERD Link or Image]

```

---
