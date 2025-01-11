import os
from pymongo import MongoClient
from app.core.config import Config

config = Config()

if os.getenv("TESTING", "false").lower() == "true":
    from mongomock import MongoClient
else:
    from pymongo import MongoClient

try:
    client = MongoClient(config.DATABASE_URL, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    db = client[config.DATABASE_NAME]
except Exception as e:
    raise RuntimeError(f"Failed to connect to the database: {e}")