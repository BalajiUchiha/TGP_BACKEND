from flask import Flask, request, jsonify
import os
from pymongo import MongoClient
from dotenv import load_dotenv
app = Flask(__name__)

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")

# Replace <password> with your actual password
client = MongoClient(f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.1my83px.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["Demo"]
users_collection = db["users"]

@app.route("/login", methods=["POST","GET"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = users_collection.find_one({"username": username, "password": password})

    if user:
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
