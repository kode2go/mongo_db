from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017")  # Replace with your MongoDB connection URI

# Create or access the "mydb" database
db = client["mydb"]

# Create or access the "users" and "posts" collections
usersCollection = db["users"]
postsCollection = db["posts"]

# Insert user documents
usersCollection.insert_many([
    { "_id": 1, "username": "user1", "name": "John" },
    { "_id": 2, "username": "user2", "name": "Jane" },
    # ... other user documents
])

# Insert post documents with references to users
postsCollection.insert_many([
    { "title": "Post 1", "content": "This is the first post.", "author_id": 1 },
    { "title": "Post 2", "content": "Another post by user1.", "author_id": 1 },
    { "title": "Post 3", "content": "A post by user2.", "author_id": 2 },
    # ... other post documents
])

# Query to retrieve all posts by a specific user (e.g., user with _id 1)
userPosts = postsCollection.find({ "author_id": 1 })

for post in userPosts:
    print(f"Post Title: {post['title']}, Content: {post['content']}")

# Query to retrieve the author information for a specific post (e.g., post with title "Post 3")
postAuthor = postsCollection.aggregate([
    {
        "$match": { "title": "Post 3" },
    },
    {
        "$lookup": {
            "from": "users",  # The collection to join with
            "localField": "author_id",  # The field from the "posts" collection
            "foreignField": "_id",  # The field from the "users" collection
            "as": "author",  # The alias for the joined data
        },
    },
    {
        "$unwind": "$author",  # Flatten the author array
    },
    {
        "$project": {
            "title": 1,
            "content": 1,
            "author.username": 1,
            "author.name": 1,
        },
    },
])

for post in postAuthor:
    print(f"Post Title: {post['title']}, Content: {post['content']}")
    print(f"Author Username: {post['author']['username']}, Name: {post['author']['name']}")
