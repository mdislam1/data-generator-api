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
    
    # Create a list of dictionaries to store the data
    data = []
    for _ in range(num_records):
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
        data.append(record)
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    return df

# Example usage
if __name__ == "__main__":
    # Generate 100 records of random data
    generate_random_data(100)
    