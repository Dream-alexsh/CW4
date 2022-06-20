from flask import request, redirect, url_for
from flask_restx import Resource, Namespace, abort

from implemented import auth_service, user_service
from project.dao.serialization.user import UserSchema
from project.exceptions import ItemNotFound, IncorrectPassword
from project.views.auth import auth_ns

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_service.auth_required
    def get(self):
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            email = auth_service.get_email_from_token(token)

            user = user_service.get_by_email(email)
            user_dict = UserSchema().dump(user)
            return user_dict, 200
        except ItemNotFound:
            abort(404, 'User not found')

    @auth_service.auth_required
    def patch(self):
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            email = auth_service.get_email_from_token(token)

            updated_data = UserSchema().dump(request.json)
            user_service.update(updated_data, email)
            return "", 200
        except ItemNotFound:
            abort(404, 'User not found')


@user_ns.route('/password/')
class PasswordView(Resource):
    @auth_service.auth_required
    def put(self):
        try:
            auth_data = request.headers['Authorization']
            token = auth_data.split("Bearer ")[-1]
            email = auth_service.get_email_from_token(token)

            passwords = request.json
            user_service.update_password(passwords, email)
            return "", 200
        except ItemNotFound:
            abort(404, 'User not found')
        except IncorrectPassword:
            abort(401, 'Password is incorrect')


