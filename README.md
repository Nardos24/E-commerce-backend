
```markdown
# FastAPI User and Product Management API

This FastAPI application provides a simple RESTful API for managing users and products. It supports CRUD operations and uses CSV files for data storage.

## Features

- **User Management**: Create, read, update, and delete users.
- **Product Management**: Create, read, update, and delete products.
- **CSV Storage**: Data is stored in CSV files for easy access and manipulation.
- **CORS Support**: Cross-Origin Resource Sharing (CORS) is enabled to allow requests from any origin.
- **Caching**: Uses caching to improve performance for frequent reads.

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn (for serving the application)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nardos24/E-commerce-backend.git
   cd E-commerce-backend
   ```

2. Install the required packages:
   ```bash
   pip install fastapi uvicorn
   ```

## Running the Application

Run the FastAPI application using Uvicorn:

```bash
uvicorn app:app --reload
```

## API Documentation

Visit `/docs` in your browser after running the application to access automatically generated API documentation. This documentation provides an interactive interface for testing the API endpoints.

## API Endpoints

### Users

- **List Users**
  - **URL**: `GET /users`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Kebede",
        "email": "nani@gmail.com"
      },
      {
        "id": 3,
        "name": "Abebe",
        "email": "abebe@example.com"
      },
      {
        "id": 4,
        "name": "lelise",
        "email": "leli54@gmail.com"
      },
      {
        "id": 8,
        "name": "bereket",
        "email": "beki@gmail.com"
      },
      {
        "id": 9,
        "name": "alem",
        "email": "alem@gmail.com"
      },
      {
        "id": 10,
        "name": "genet",
        "email": "geni2024@gmail.com"
      }
    ]
    ```

- **Get User by ID**
  - **URL**: `GET /users/{user_id}`
  - **Response** (for example, if `user_id` is `1`):
    ```json
    {
      "id": 1,
      "name": "Kebede",
      "email": "nani@gmail.com"
    }
    ```
  - **Error Response** (if user not found):
    ```json
    {
      "detail": "User not found."
    }
    ```

- **Add User (POST)**
  - **URL**: `POST /users`
  - **Request Body**:
    ```json
    {
      "id": 2,
      "name": "Jane Doe",
      "email": "jane@example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 2,
      "name": "Jane Doe",
      "email": "jane@example.com"
    }
    ```

- **Update User (PUT)**
  - **URL**: `PUT /users/{user_id}`
  - **Request Body**:
    ```json
    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Error Response** (if user not found):
    ```json
    {
      "detail": "User not found."
    }
    ```

- **Delete User (DELETE)**
  - **URL**: `DELETE /users/{user_id}`
  - **Response** (for deleted user):
    ```json
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
  - **Error Response** (if user not found):
    ```json
    {
      "detail": "User not found."
    }
    ```

### Products

- **List Products**
  - **URL**: `GET /products`
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "name": "orange",
        "price": 10.9,
        "stock": 10
      },
      {
        "id": 2,
        "name": "pineapple",
        "price": 10.0,
        "stock": 60
      },
      {
        "id": 6,
        "name": "apple",
        "price": 20.0,
        "stock": 5
      },
      {
        "id": 3,
        "name": "cabbage",
        "price": 50.0,
        "stock": 1
      }
    ]
    ```

- **Get Product by ID**
  - **URL**: `GET /products/{product_id}`
  - **Response** (for example, if `product_id` is `1`):
    ```json
    {
      "id": 1,
      "name": "orange",
      "price": 10.9,
      "stock": 10
    }
    ```
  - **Error Response** (if product not found):
    ```json
    {
      "detail": "Product not found."
    }
    ```

- **Add Product (POST)**
  - **URL**: `POST /products`
  - **Request Body**:
    ```json
    {
      "id": 4,
      "name": "banana",
      "price": 5.0,
      "stock": 30
    }
    ```
  - **Response**:
    ```json
    {
      "id": 4,
      "name": "banana",
      "price": 5.0,
      "stock": 30
    }
    ```

- **Update Product (PUT)**
  - **URL**: `PUT /products/{product_id}`
  - **Request Body**:
    ```json
    {
      "price": 15.0,
      "stock": 20
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "name": "orange",
      "price": 15.0,
      "stock": 20
    }
    ```
  - **Error Response** (if product not found):
    ```json
    {
      "detail": "Product not found."
    }
    ```

- **Delete Product (DELETE)**
  - **URL**: `DELETE /products/{product_id}`
  - **Response** (for deleted product):
    ```json
    {
      "id": 1,
      "name": "orange",
      "price": 10.9,
      "stock": 10
    }
    ```
  - **Error Response** (if product not found):
    ```json
    {
      "detail": "Product not found."
    }
    ```

## Testing the API

You can test the API using tools like [Postman] or [cURL].
 some example requests:

### Example Requests

1. **List Users**
   ```bash
   curl -X GET http://localhost:8000/users
   ```

2. **Get User by ID**
   ```bash
   curl -X GET http://localhost:8000/users/1
   ```

3. **Add User**
   ```bash
   curl -X POST http://localhost:8000/users -H "Content-Type: application/json" -d '{"id": 2, "name": "Jane Doe", "email": "jane@example.com"}'
   ```

4. **Update User**
   ```bash
   curl -X PUT http://localhost:8000/users/2 -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane.smith@example.com"}'
   ```

5. **Delete User**
   ```bash
   curl -X DELETE http://localhost:8000/users/2
   ```

6. **List Products**
   ```bash
   curl -X GET http://localhost:8000/products
   ```

7. **Get Product by ID**
   ```bash
   curl -X GET http://localhost:8000/products/1
   ```

8. **Add Product**
   ```bash
   curl -X POST http://localhost:8000/products -H "Content-Type: application/json" -d '{"id": 4, "name": "banana", "price": 5.0, "stock": 30}'
   ```

9. **Update Product**
   ```bash
   curl -X PUT http://localhost:8000/products/1 -H "Content-Type: application/json" -d '{"price": 15.0, "stock": 20}'
   ```

10. **Delete Product**
    ```bash
    curl -X DELETE http://localhost:8000/products/1
    ```

## Caching

The application uses a caching mechanism to store users and products in memory for efficient retrieval. The Cache-Control header is set to allow caching for 60 seconds.

