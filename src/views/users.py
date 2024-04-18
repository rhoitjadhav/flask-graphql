from flask import Blueprint, request

from src.schemas.users_schema import UsersSchema
from src.services.users_service import UsersService

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("", methods=["GET"])
def get_users():
    return UsersService.get_users()


@bp.route("/<int:id>", methods=["GET"])
def get_user(id):
    return UsersService.get_user(id)


@bp.route("", methods=["POST"])
def create_user():
    payload = request.get_json()
    user = UsersSchema(**payload)
    return UsersService.create_user(user)


@bp.route("", methods=["PUT"])
def update_user():
    return []


@bp.route("", methods=["DELETE"])
def delete_user():
    return []
