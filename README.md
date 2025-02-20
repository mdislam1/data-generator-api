# Random Data Generator and API

## Overview
This project consists of two Python scripts:
1. **`data_generator.py`**: Generates random data for people using the `Faker` library.
2. **`api.py`**: Provides a RESTful API to interact with the generated data (retrieve, update, and delete records).

The project is designed to demonstrate how to generate random data and expose it via a simple API using Python and Flask. It is a great starting point for learning about data generation, REST APIs, and working with Python libraries like `pandas` and `Faker`.

---

## Features
- **Random Data Generation**: Generates random data for people, including first name, last name, address, city, state, zip code, email, and phone number.
- **RESTful API**: Provides endpoints to:
  - Retrieve all people.
  - Retrieve a specific person by ID.
  - Update a person's details.
  - Delete a person.

---

## Prerequisites
- Python 3.x
- Required Python libraries: `Flask`, `pandas`, `Faker`

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mdislam1/api-python.git
   cd your-repo-name
   ```

2. **Install Dependencies Using `requirements.txt`**:
   - Open a terminal or command prompt.
   - Navigate to the project directory:
     ```bash
     cd path/to/data-generator-api
     ```
   - Run the following command to install the dependencies:
     ```bash
     pip install -r requirements.txt
     ```

---

## Running the Scripts

### 1. Generate Random Data
Run the `data_generator.py` script to generate random data:
```bash
python data_generator.py
```
- This script generates a DataFrame with 100 random records by default.

---

### 2. Start the API
Run the `api.py` script to start the Flask API:
```bash
python api.py
```
- The API will be accessible at `http://127.0.0.1:5000`.

---

## API Endpoints

### 1. **Get All People**
- **Endpoint**: `GET /people`
- **Description**: Retrieves all people in the dataset.
- **Example**:
  ```bash
  curl http://127.0.0.1:5000/people
  ```

### 2. **Get a Specific Person by ID**
- **Endpoint**: `GET /people/<id>`
- **Description**: Retrieves the details of a specific person by their ID.
- **Example**:
  ```bash
  curl http://127.0.0.1:5000/people/0
  ```

### 3. **Update a Person**
- **Endpoint**: `PUT /people/<id>`
- **Description**: Updates the details of a specific person by their ID.
- **Example**:
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d "{\"first_name\": \"John\", \"city\": \"New York\"}" http://127.0.0.1:5000/people/0
  ```

### 4. **Delete a Person**
- **Endpoint**: `DELETE /people/<id>`
- **Description**: Deletes a specific person by their ID.
- **Example**:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/people/0
  ```

---

## Running on Different Operating Systems

### Windows
1. Open **Command Prompt** or **PowerShell**.
2. Navigate to the project directory:
   ```cmd
   cd path\to\your-repo-name
   ```
3. Run the scripts as described above.

### macOS/Linux
1. Open **Terminal**.
2. Navigate to the project directory:
   ```bash
   cd path/to/your-repo-name
   ```
3. Run the scripts as described above.

---

## Project Structure
```
data-generator-api/
├── data_generator.py       # Script to generate random data
├── api.py                  # Script to run the API
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
```

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author
Md Islam  
GitHub: https://github.com/mdislam1

---

Enjoy using the Random Data Generator and API! 🚀
