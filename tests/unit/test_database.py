
from pymongo.errors import ConnectionFailure
from app.infrastructure.database.database import client

def test_mongo_connection():
    try:
        client.admin.command('ping')
        assert True
    except ConnectionFailure:
        assert False
