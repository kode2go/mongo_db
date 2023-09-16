# Create a list of product dictionaries
products = [
    {
        "_id": "5f5b968c7dca2e6d8762b3d1",
        "product_name": "Premium Laptop",
        "category": "Electronics",
        "price": 1099.99,
        "description": "A high-performance laptop for professionals.",
        "specifications": {
            "processor": "Intel Core i7",
            "memory": "16GB DDR4 RAM",
            "storage": "512GB SSD",
            "display": "15.6-inch Full HD",
            "graphics": "NVIDIA GeForce GTX 1650",
            "operating_system": "Windows 10 Pro"
        },
        "reviews": [
            {
                "username": "happy_customer",
                "rating": 5,
                "comment": "I love this laptop! Fast and reliable."
            },
            {
                "username": "tech_guru",
                "rating": 4,
                "comment": "Great specs, but a bit heavy for my liking."
            }
        ],
        "stock": {
            "available": 50,
            "location": "Warehouse A",
            "last_restocked": "2023-08-10T14:00:00Z"
        },
        "tags": ["laptop", "electronics", "performance"],
        "related_products": [
            "5f5b968c7dca2e6d8762b3d2",
            "5f5b968c7dca2e6d8762b3d3",
        ],
        "shipping_info": {
            "weight": "3.5 kg",
            "dimensions": "20 x 15 x 1.5 inches",
            "shipping_available": True
        }
    },
    # Add the other product dictionaries (product2, product3, product4) here
    {
        "_id": "5f5b968c7dca2e6d8762b3d4",
        "product_name": "Smartphone X",
        "category": "Electronics",
        "price": 699.99,
        "description": "A high-end smartphone with cutting-edge features.",
        "specifications": {
            "processor": "Snapdragon 888",
            "memory": "8GB RAM",
            "storage": "256GB",
            "display": "6.5-inch AMOLED",
            "camera": "Triple camera setup",
            "operating_system": "Android 12"
        },
        "reviews": [
            {
                "username": "mobile_enthusiast",
                "rating": 5,
                "comment": "This smartphone is amazing! Great camera and performance."
            },
            {
                "username": "tech_lover",
                "rating": 4,
                "comment": "Impressive specs, but a bit pricey."
            }
        ],
        "stock": {
            "available": 30,
            "location": "Warehouse B",
            "last_restocked": "2023-08-12T10:30:00Z"
        },
        "tags": ["smartphone", "electronics", "flagship"],
        "related_products": [
            "5f5b968c7dca2e6d8762b3d1",
            "5f5b968c7dca2e6d8762b3d5"  # Another product's ObjectId
        ],
        "shipping_info": {
            "weight": "0.2 kg",
            "dimensions": "6.2 x 3.0 x 0.3 inches",
            "shipping_available": True
        }
    },

{
    "_id": "5f5b968c7dca2e6d8762b3d6",
    "product_name": "Fitness Tracker Pro",
    "category": "Wearable Tech",
    "price": 99.99,
    "description": "Track your fitness goals with this advanced wearable device.",
    "specifications": {
        "sensors": "Heart rate, GPS, Accelerometer",
        "display": "Color touchscreen",
        "battery_life": "Up to 7 days",
        "compatibility": "iOS and Android"
    },
    "reviews": [
        {
            "username": "fitness_enthusiast",
            "rating": 4,
            "comment": "Great for tracking workouts and monitoring health."
        },
        {
            "username": "casual_user",
            "rating": 5,
            "comment": "Easy to use and comfortable to wear."
        }
    ],
    "stock": {
        "available": 100,
        "location": "Warehouse C",
        "last_restocked": "2023-08-15T09:15:00Z"
    },
    "tags": ["fitness", "wearable", "health"],
    "related_products": [],
    "shipping_info": {
        "weight": "0.05 kg",
        "dimensions": "1.2 x 1.2 x 0.3 inches",
        "shipping_available": True
    }
},

{
    "_id": "5f5b968c7dca2e6d8762b3d7",
    "product_name": "Coffee Maker Deluxe",
    "category": "Kitchen Appliances",
    "price": 79.99,
    "description": "Brew your favorite coffee with ease using this deluxe coffee maker.",
    "specifications": {
        "capacity": "12 cups",
        "brewing_type": "Drip",
        "color": "Stainless steel",
        "auto_shutdown": "Yes",
        "warranty": "2 years"
    },
    "reviews": [
        {
            "username": "coffee_lover",
            "rating": 5,
            "comment": "Makes great coffee and keeps it hot!"
        },
        {
            "username": "kitchen_chef",
            "rating": 4,
            "comment": "Easy to use and clean."
        }
    ],
    "stock": {
        "available": 20,
        "location": "Warehouse D",
        "last_restocked": "2023-08-18T08:45:00Z"
    },
    "tags": ["coffee", "appliance", "kitchen"],
    "related_products": [],
    "shipping_info": {
        "weight": "3.2 kg",
        "dimensions": "10.5 x 8.0 x 14.0 inches",
        "shipping_available": True
    }
}
]

# Query: Find Electronics Products with High Ratings
electronics_high_ratings = [product for product in products if product["category"] == "Electronics" and any(review["rating"] >= 4 for review in product["reviews"])]

# Query: Find Products with Similar Specifications
similar_specifications = [
    product for product in products if
    product.get("specifications", {}).get("processor") == "Intel Core i7" and
    product.get("specifications", {}).get("memory") == "16GB DDR4 RAM"
]
# Query: Find Products with Available Stock
available_stock = [product for product in products if product["stock"]["available"] > 0]

# Query: Find Related Products by Tags (Example with "performance" tag)
related_by_tags = [product for product in products if "performance" in product["tags"]]

# Query: Find Products with Free Shipping
free_shipping = [product for product in products if product["shipping_info"]["shipping_available"]]

# Print results of queries
print("Electronics Products with High Ratings:")
for product in electronics_high_ratings:
    print(product["product_name"])

print("\nProducts with Similar Specifications:")
for product in similar_specifications:
    print(product["product_name"])

print("\nProducts with Available Stock:")
for product in available_stock:
    print(product["product_name"])

print("\nRelated Products by Tags:")
for product in related_by_tags:
    print(product["product_name"])

print("\nProducts with Free Shipping:")
for product in free_shipping:
    print(product["product_name"])
