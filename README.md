# Flask API with Enhanced Routing

## Project Overview
This project is a Flask-based API with enhanced routing and structured error handling. The API supports CRUD operations for a sample resource (`items`) and includes features such as input validation and custom error responses.

---

## Endpoints

### 1. **GET /items**
- **Description**: Fetch all items.
- **Response**:
  - Status Code: `200 OK`
  - Body:
    ```json
    []
    ```
    or
    ```json
    [
      {
        "id": 1,
        "name": "Sample Item",
        "description": "Sample description."
      }
    ]
    ```

---

### 2. **POST /items**
- **Description**: Add a new item.
- **Request**:
  - Method: `POST`
  - Body (JSON):
    ```json
    {
      "name": "Test Item",
      "description": "Test description."
    }
    ```
- **Response**:
  - Status Code: `201 Created`
  - Body:
    ```json
    {
      "id": 1,
      "name": "Test Item",
      "description": "Test description."
    }
    ```
- **Errors**:
  - Missing fields:
    ```json
    {
      "errors": {
        "name": "Field is required.",
        "description": "Field is required."
      }
    }
    ```

---

### 3. **GET /items/<item_id>**
- **Description**: Fetch a specific item by `item_id`.
- **Response**:
  - **If Found**:
    ```json
    {
      "id": 1,
      "name": "Sample Item",
      "description": "Sample description."
    }
    ```
  - **If Not Found**:
    ```json
    {
      "error": "Item not found"
    }
    ```

---

### 4. **PUT /items/<item_id>**
- **Description**: Update a specific item by `item_id`.
- **Request**:
  - Body (JSON):
    ```json
    {
      "name": "Updated Item",
      "description": "Updated description."
    }
    ```
- **Response**:
  - **If Successful**:
    ```json
    {
      "id": 1,
      "name": "Updated Item",
      "description": "Updated description."
    }
    ```
  - **If Not Found**:
    ```json
    {
      "error": "Item not found"
    }
    ```

---

### 5. **DELETE /items/<item_id>**
- **Description**: Delete a specific item by `item_id`.
- **Response**:
  - **If Successful**:
    ```json
    {
      "message": "Item deleted"
    }
    ```
  - **If Not Found**:
    ```json
    {
      "error": "Item not found"
    }
    ```

---

## Setup and Installation

### Prerequisites
- Python 3.7+
- Flask

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd flask-api
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   flask run
   ```
4. The API will be available at `http://127.0.0.1:5000`.

---

## Testing

### Manual Testing
Use Postman, Hoppscotch, or curl to test the endpoints.

### Example with curl
- **GET /items**:
  ```bash
  curl http://127.0.0.1:5000/items
  ```
- **POST /items**:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "Test", "description": "Test description"}' http://127.0.0.1:5000/items
  ```

---

## Implementation Details

### Code Structure
```plaintext
flask-api/
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── routes.py           # All route definitions
│   ├── error_handlers.py   # Error handler functions
│   ├── models/
│   │   └── item.py         # Item model definition
│   ├── schemas/
│   │   └── item_schema.py  # Validation logic
├── tests/
│   └── test_endpoints.py   # Unit tests for endpoints
├── postman/                # Postman collection for testing
│   └── collection.json
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── .gitignore
```

### Design Choices
- **Validation**: Used a schema-based approach to ensure clean input handling.
- **Error Handling**: Provided structured and meaningful error messages for better debugging.

---

## Known Issues
- In-memory storage (`items` list) is not persistent.
- No authentication or authorization implemented.

---

## Future Improvements
1. Add database integration (e.g., SQLite, PostgreSQL).
2. Implement authentication and authorization.
3. Use Flask-Migrate for database migrations.
4. Add comprehensive unit and integration tests.

---

## License
This project is licensed under the MIT License.

