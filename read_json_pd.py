import pandas as pd
import json

# Read the products from the JSON file into a Pandas DataFrame
with open("dummy_products.json", "r") as json_file:
    data = json.load(json_file)

df = pd.DataFrame(data)

# Now you can perform queries using Pandas DataFrame operations
# Example: Find Electronics Products with High Ratings
electronics_high_ratings = df[(df["category"] == "Electronics") & (df["reviews"].apply(lambda x: any(review["rating"] >= 4 for review in x)))]

# Print the results
print("Electronics Products with High Ratings:")
print(electronics_high_ratings[["product_name"]])
