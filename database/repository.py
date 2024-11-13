from database.connection import get_database

db = get_database()
black_list_collection = db['black_list']
def insert_to_black_list(black_transaction):
    result = black_list_collection.insert_one(black_transaction)
    return result.inserted_id

def get_black_list():
    return list(black_list_collection.find({}, {'_id': 0}).limit(25))