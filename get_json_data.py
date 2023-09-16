import json

# Read the products from the JSON file
with open("dummy_products.json", "r") as json_file:
    products = json.load(json_file)

# Query: Find Electronics Products with High Ratings
electronics_high_ratings = [product for product in products if product["category"] == "Electronics" and any(review["rating"] >= 4 for review in product["reviews"])]

# Query: Find Products with Similar Specifications
similar_specifications = [product for product in products if product["specifications"]["processor"] == "Intel Core i7" and product["specifications"]["memory"] == "16GB DDR4 RAM"]

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
