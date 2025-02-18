import logging

from bson import ObjectId
from bson.errors import InvalidId

from app import mongo, bcrypt


def add_user(user_data):
    if not isinstance(user_data, dict):
        logging.error("Invalid data format")
        return {"error": "Invalid data format"}

    email, password, name = user_data.get("email"), user_data.get("password"), user_data.get("name")

    if not all([email, password, name]):
        logging.warning("Missing required fields.")
        return {"error": "Missing required fields (name, email, password)"}

    if mongo.db.users.find_one({"email": email}):
        logging.warning(f"Email {email} already exists.")
        return {"error": "Email already exists"}

    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
    user_id = mongo.db.users.insert_one({
        "name": name,
        "email": email,
        "password": hashed_pw
    }).inserted_id

    logging.info(f"User created with ID: {user_id}")
    return str(user_id)


def fetch_all_users():
    users = list(mongo.db.users.find({}, {"password": 0}))
    logging.info(f"Fetched {len(users)} users.")
    return users


def fetch_user_by_id(user_id):
    try:
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)}, {"password": 0})
        if user:
            logging.info(f"User found with ID: {user_id}")
        else:
            logging.warning(f"User not found with ID: {user_id}")
        return user
    except InvalidId:
        logging.error(f"Invalid user ID: {user_id}")
        return {"error": "Invalid user ID format"}


def modify_user(user_id, update_data):
    if not isinstance(update_data, dict):
        logging.error("Invalid update data format")
        return {"error": "Invalid data format"}

    if not ObjectId.is_valid(user_id):
        logging.warning(f"Invalid ID: {user_id}")
        return {"error": "Invalid user ID format"}

    result = mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    if result.modified_count:
        logging.info(f"User {user_id} updated.")
        return {"message": "User updated"}

    logging.warning(f"User not found with ID: {user_id}")
    return {"error": "User not found"}


def remove_user(user_id):
    if not ObjectId.is_valid(user_id):
        logging.warning(f"Invalid ID: {user_id}")
        return {"error": "Invalid user ID format"}

    result = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count:
        logging.info(f"User {user_id} deleted.")
        return {"message": "User deleted"}

    logging.warning(f"User not found with ID: {user_id}")
    return {"error": "User not found"}
