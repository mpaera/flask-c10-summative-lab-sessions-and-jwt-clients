from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from server import db
from server.models.user import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.post("/register")
def register():
    data = request.get_json() or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409

    user = User(username=username)
    user.password = password

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "id": user.id,
        "username": user.username
    }), 201


@auth_bp.post("/login")
def login():
    data = request.get_json() or {}

    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,
        "user": {
            "id": user.id,
            "username": user.username
        }
    }), 200
