# data_generator.py
import pandas as pd
from faker import Faker

def generate_random_data(num_records=100):
    """
    Generates random data for people using the Faker library.

    Args:
        num_records (int): Number of records to generate. Default is 100.

    Returns:
        pd.DataFrame: A DataFrame containing the generated data.
    """
    fake = Faker()

    # Create a set to track unique values for specific fields
    unique_first_names = set()
    unique_last_names = set()
    unique_addresses = set()
    unique_emails = set()
    unique_phone_numbers = set()

    
    # Create a list of dictionaries to store the data
    data = []
    while len(data) < num_records:
        record = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state_abbr(),
            "zip_code": fake.zipcode(),
            "email": fake.email(),
            "phone_number": fake.phone_number()
        }

        # Check for uniqueness of required fields
        if (record["first_name"] not in unique_first_names and
            record["last_name"] not in unique_last_names and
            record["address"] not in unique_addresses and
            record["email"] not in unique_emails and
            record["phone_number"] not in unique_phone_numbers):


            # Add the record to the data list
            data.append(record)

            # Update the sets with the new unique values
            unique_first_names.add(record["first_name"])
            unique_last_names.add(record["last_name"])
            unique_addresses.add(record["address"])
            unique_emails.add(record["email"])
            unique_phone_numbers.add(record["phone_number"])
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # Generate 10,000 records of random data
    print(generate_random_data(100))
    