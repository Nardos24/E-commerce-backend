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
## running the application
```bash
uvicorn main:app --reload
