from pymongo import MongoClient
from faker import Faker
import random

# Initialize the MongoDB client
client = MongoClient('localhost', 27017)  # Replace with your MongoDB server details
db = client.mydb  # Replace 'mydb' with your desired database name

# Create a User collection
User = db.User

# Initialize the Faker library
fake = Faker()

# Generate and insert dummy user data
for _ in range(10):
    user_data = {
        'username': fake.user_name(),
        'name': fake.name(),
        'email': fake.email(),
        'tweets': []
    }

    # Generate 3 to 5 dummy tweets for each user
    for _ in range(random.randint(3, 5)):
        user_data['tweets'].append(fake.text(max_nb_chars=140))  # Generate a tweet

    User.insert_one(user_data)

# Query the database to retrieve and print user data
for user in User.find():
    print(user)

# Close the MongoDB client connection
client.close()
