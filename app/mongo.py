import pymongo

client = pymongo.MongoClient("mongodb+srv://kshitij:kshitij@cluster0.rhimj.mongodb.net/?retryWrites=true&w=majority")
db = client.enigma

def get_user_by_email(email):
    users = db.users
    return users.find_one({'email': email})

def get_workspace_by_name(name):
    workspaces = db.workspaces
    return workspaces.find_one({'name': name})

def create_user(user):
    users = db.users
    user_id = users.insert_one(user).inserted_id
    return str(user_id)

def create_workspace(workspace):
    workspaces = db.workspaces
    workspace_id = workspaces.insert_one(workspace)

    users = db.users
    users.update_one({"email": email}, {"$push": {"workspaces": { 
        "name": workspace["name"],
        "id": workspace_id,
        "datasets": []
    }}})

    return workspace_id
    