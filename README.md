# Voucher Management System

This project is a Voucher Management System developed using FastAPI and SQLite.
It provides endpoints for creating, updating, activating, deactivating, and redeeming vouchers.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Faresa/voucher-management.git
   ```

2. Navigate to the project directory:

   ```bash
   cd voucher-management
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

## Endpoints

## Management Interface Endpoints

#### Create a Voucher

- **URL**: `http://localhost:8000/management/create_voucher`
- **Method**: `POST`
- **Parameters**:
  ```Parameters
  {
      "code": "VOUCHER_CODE",
      "redemption_limit": 10,
      "expiration_date": "2024-12-31T23:59:59",
      "active": true
  }
  ```
- **Description**: Creates a new voucher with the provided details.

#### Get a Voucher

- **URL**: `http://localhost:8000/management/get_voucher/{code}`
- **Method**: `GET`
- **Description**: Retrieves the details of a voucher by its code.

#### Update a Voucher

- **URL**: `http://localhost:8000/management/update_voucher/{code}`
- **Method**: `PUT`
- **Parameters**:
  ```Parameters
  {
      "redemption_limit": 20,
      "expiration_date": "2025-12-31T23:59:59",
      "active": true
  }
  ```
- **Description**: Updates the details of a voucher by its code.

#### Delete a Voucher

- **URL**: `http://localhost:8000/management/delete_voucher/{code}`
- **Method**: `DELETE`
- **Description**: Deletes a voucher by its code.

#### Activate a Voucher

- **URL**: `http://localhost:8000/management/activate_voucher/{code}`
- **Method**: `PUT`
- **Description**: Activates a voucher by its code.

#### Deactivate a Voucher

- **URL**: `http://localhost:8000/management/deactivate_voucher/{code}`
- **Method**: `PUT`
- **Description**: Deactivates a voucher by its code.

#### List all Voucers

- **URL**: `http://localhost:8000/management/list_all_vouchers`
- **Method**: `GET`
- **Description**: Get a list of all the vouchers.

  
### Redemption Interface Endpoints

#### Redeem a Voucher

- **URL**: `http://localhost:8000/redemption/redeem_voucher/{code}`
- **Method**: `POST`
- **Description**: Redeems a voucher by its code.

### Code Structure:

1. **Main Application Directory (`voucher_management/`)**:
   - Contains the main application code and configuration files.
   - Includes subdirectories for different modules and components.

2. **API Directory (`api/`)**:
   - Houses all API-related files, including routers, endpoints, and request handlers.
   - Organized into subdirectories based on different features or resource types.

3. **Database Directory (`database/`)**:
   - Contains database-related files, including database initialization and models.
   - Includes subdirectories for different types of databases, such as SQL and NoSQL.

4. **Models Directory (`models/`)**:
   - Defines the data models used within the application.
   - Organized into separate modules for each data entity or resource.

5. **Configuration Files**:
   - `requirements.txt`: Lists all Python dependencies required to run the application.
   - `README.md`: Contains instructions for setting up and running the project, as well as an overview of the code structure and design choices.

### Design Choices:

1. **Framework**: 
   - FastAPI is chosen as the web framework for its performance, simplicity, and support for modern Python features like type annotations.

2. **Database**:
   - SQLite is chosen as the database engine for its simplicity and lightweight nature, suitable for small to medium-sized applications.

3. **Code Structure**:
   - Modular design with separate directories for different components allows for better organization and maintainability of the codebase.

4. **Asynchronous I/O**:
   - Using asynchronous frameworks like FastAPI and asynchronous database libraries allows for handling multiple concurrent requests efficiently.

5. **Data Models**:
   - Data models are defined using SQLAlchemy ORM for easy interaction with the database and to ensure data integrity.

6. **RESTful API**:
   - Endpoints follow RESTful principles for clear and predictable API design, making it easier for clients to interact with the application.

7. **Error Handling**:
   - Custom error handling ensures informative and consistent error responses, enhancing the usability of the API.

8. **Documentation**:
   - Comprehensive README.md file includes setup instructions, API documentation, and explanations of code structure and design choices, aiding developers in understanding and contributing to the project.

These design choices aim to create a scalable, maintainable, and well-documented application that meets the requirements of the project.


## License

This project is licensed under the [MIT License](LICENSE).
