from flask import jsonify, make_response

from src import db
from src.schemas.users_schema import UsersSchema
from src.repositories.users_repository import UsersRepository


class UsersService:
    @staticmethod
    def get_users():
        users = UsersRepository.get_all()
        return make_response(jsonify([user.as_dict() for user in users]), 200)

    @staticmethod
    def get_user(user_id):
        user = UsersRepository.get_by_id(user_id)
        if user:
            return make_response(jsonify(user.as_dict()), 200)
        return make_response(jsonify({"message": "user not found"}), 404)

    @staticmethod
    def create_user(user: UsersSchema):
        user = UsersRepository(user.username, user.name, user.email, user.password)
        db.session.add(user)
        db.session.commit()
        return make_response(jsonify({"message": "user created"}), 201)

    @staticmethod
    def update_user(user: UsersSchema):
        if not UsersRepository.update(user.id, user):
            return make_response(jsonify({"message": "user not found"}), 404)
        return make_response(jsonify({"message": "user details updated"}), 201)

    @staticmethod
    def delete_user(user_id: int):
        UsersRepository.delete(user_id)
        return make_response(jsonify({"message": "user deleted"}), 201)
