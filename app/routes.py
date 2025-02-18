from bson import ObjectId
from flask import Blueprint, request, jsonify

from app import serializer
from app.services import fetch_all_users, remove_user, modify_user, fetch_user_by_id, add_user

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/users", methods=["GET"])
def get_users():
    users = fetch_all_users()
    return jsonify([serializer(user) for user in users]), 200


@user_routes.route("/users/<string:user_id>", methods=["GET"])
def get_user(user_id):
    if not ObjectId.is_valid(user_id):
        return jsonify({"error": "Invalid user ID format"}), 400

    user = fetch_user_by_id(user_id)
    if user:
        return jsonify(serializer(user))
    return jsonify({"error": "User not found"}), 404


@user_routes.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body is missing"}), 400

    result = add_user(data)
    if "error" in result:
        return jsonify(result), 400

    return jsonify({"message": "User created", "id": result}), 201


@user_routes.route("/users/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    if not ObjectId.is_valid(user_id):
        return jsonify({"error": "Invalid user ID format"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body is missing"}), 400

    result = modify_user(user_id, data)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 400

    return jsonify({"message": "User updated"}), 200


@user_routes.route("/users/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if not ObjectId.is_valid(user_id):
        return jsonify({"error": "Invalid user ID format"}), 400

    result = remove_user(user_id)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 404

    return jsonify({"message": "User deleted"}), 200
