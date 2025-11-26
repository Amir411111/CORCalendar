import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
# Mask password for printing
masked_uri = mongo_uri.replace("SepqZM9YulYjynk", "******")
print(f"Testing connection to: {masked_uri}")

try:
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    # Trigger a connection
    client.admin.command('ping')
    print("SUCCESS: Connected to MongoDB!")
except Exception as e:
    print(f"ERROR: Failed to connect. Reason: {e}")
