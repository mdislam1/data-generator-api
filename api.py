# api.py
from flask import Flask, jsonify, request
from data_generator import generate_random_data

# Initialize Flask app
app = Flask(__name__)

# Generate random data using the data_generator module
data = generate_random_data(100)  # Generate 100 records

@app.route("/people", methods=["GET"])
def get_all_people():
    """
    Endpoint to retrieve all people in the dataset.
    """
    # Convert the DataFrame to a list of dictionaries
    people = data.to_dict(orient="records")
    return jsonify(people)

@app.route("/people/<int:id>", methods=["GET"])
def get_person_by_id(id):
    """
    Endpoint to retrieve a specific person by their index (ID).
    """
    if id < 0 or id >= len(data):
        return jsonify({"error": "Invalid ID"}), 404
    
    # Get the person by index
    person = data.iloc[id].to_dict()
    return jsonify(person)

@app.route("/people/<int:id>", methods=["PUT"])
def update_person(id):
    """
    Endpoint to update an existing person by their index (ID).
    """
    if id < 0 or id >= len(data):
        return jsonify({"error": "Invalid ID"}), 404
    
    # Get the JSON data from the request
    update_data = request.json
    
    # Update the person's data
    for key, value in update_data.items():
        if key in data.columns:
            data.at[id, key] = value
    
    # Return the updated person
    updated_person = data.iloc[id].to_dict()
    return jsonify(updated_person)

@app.route("/people/<int:id>", methods=["DELETE"])
def delete_person(id):
    """
    Endpoint to delete a person by their index (ID).
    """
    if id < 0 or id >= len(data):
        return jsonify({"error": "Invalid ID"}), 404
    
    # Delete the person by index
    deleted_person = data.iloc[id].to_dict()
    data.drop(index=id, inplace=True)
    data.reset_index(drop=True, inplace=True)
    
    # Return the deleted person
    return jsonify(deleted_person)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)