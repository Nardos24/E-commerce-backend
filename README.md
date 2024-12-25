# FastAPI CRUD API with CSV Storage

This project provides a simple FastAPI CRUD (Create, Read, Update, Delete) API to manage users and products, using CSV files for storage.

## Features

- **User and Product Management**: 
  - Add, update, delete, and retrieve users and products.
- **CSV Storage**: 
  - Data is stored in `users.csv` and `products.csv`.
- **Caching**: 
  - Results are cached using `lru_cache` to optimize read operations.
- **CORS Support**: 
  - Cross-Origin Resource Sharing (CORS) is enabled for all domains.
- **Cache-Control Header**: 
  - Responses are cached for 60 seconds.

## Installation

### Prerequisites

- Python 3.7+  
- Install dependencies:

```bash
pip install fastapi uvicorn pydantic

##Running the Application
uvicorn main:app --reload
