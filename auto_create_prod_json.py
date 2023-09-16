import json
from faker import Faker
import random
from datetime import datetime

# Define a custom JSON encoder to handle datetime objects
class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return super(DateTimeEncoder, self).default(o)

# Initialize the Faker library
fake = Faker()

# Create a list to store the products
products = []

# Generate and store 100 dummy products
for _ in range(100):
    product = {
        "product_name": fake.word(),  # Use non-unique words
        "category": fake.random_element(elements=("Electronics", "Clothing", "Kitchen", "Sports")),
        "price": round(random.uniform(10.0, 1000.0), 2),
        "description": fake.sentence(),
        "specifications": {
            "processor": fake.random_element(elements=("Intel Core i7", "AMD Ryzen 9", "Apple M1")),
            "memory": fake.random_element(elements=("8GB DDR4 RAM", "16GB DDR4 RAM", "32GB DDR4 RAM")),
            "storage": fake.random_element(elements=("256GB SSD", "512GB SSD", "1TB HDD")),
            "display": fake.random_element(elements=("15.6-inch Full HD", "13.3-inch Retina", "27-inch 4K")),
            "graphics": fake.random_element(elements=("NVIDIA GeForce GTX 1650", "AMD Radeon RX 5700", "Intel Iris Xe")),
        },
        "reviews": [
            {
                "username": fake.user_name(),
                "rating": random.randint(1, 5),
                "comment": fake.paragraph(),
            }
            for _ in range(random.randint(1, 5))
        ],
        "stock": {
            "available": random.randint(0, 100),
            "location": fake.random_element(elements=("Warehouse A", "Warehouse B", "Warehouse C")),
            "last_restocked": fake.date_time_this_decade(),
        },
        "tags": [fake.word() for _ in range(random.randint(1, 5))],
        "shipping_info": {
            "weight": f"{round(random.uniform(0.1, 10.0), 2)} kg",
            "dimensions": f"{round(random.uniform(5, 30), 2)} x {round(random.uniform(5, 30), 2)} x {round(random.uniform(1, 10), 2)} inches",
            "shipping_available": fake.random_element(elements=(True, False)),
        },
    }
    products.append(product)

# Save the products to a JSON file
with open("dummy_products.json", "w") as json_file:
    json.dump(products, json_file, indent=4, cls=DateTimeEncoder)

print("Dummy products have been generated and saved to 'dummy_products.json'.")
