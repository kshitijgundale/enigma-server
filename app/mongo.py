import pymongo

client = pymongo.MongoClient("mongodb+srv://kshitij:kshitij@cluster0.rhimj.mongodb.net/?retryWrites=true&w=majority")
db = client.enigma

users = db.users

def get_user_by_email(email):
    return users.find_one({'email': email})

def create_user(user):
    users = db.users
    user_id = users.insert_one(user).inserted_id
    return str(user_id)