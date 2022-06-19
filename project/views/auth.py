from flask import request
from flask_restx import Namespace, Resource, abort
from marshmallow import ValidationError

from implemented import auth_service, user_service
from project.dao.serialization.user import UserSchema
from project.exceptions import UserAlreadyExists, ItemNotFound, IncorrectPassword, InvalidToken

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class RegisterView(Resource):
    def post(self):
        users = {
            'email': request.json.get('email'),
            'password': request.json.get('password')
        }
        if None in users.values():
            abort(400, 'Wrong fields passed')

        try:
            data = UserSchema().load(users)
            user = user_service.create(data)
            return "", 201, {"location": f"/user/{user.id}"}
        except ValidationError:
            abort(400, 'Not valid data passed')
        except UserAlreadyExists:
            abort(400, 'User already exists')


@auth_ns.route('/login/')
class LoginView(Resource):
    def post(self):
        users = {
            'email': request.json.get('email'),
            'password': request.json.get('password')
        }
        if None in users.values():
            abort(400, 'Not valid data passed')

        # Generate tokens
        try:
            tokens = auth_service.generate_tokens(users)
            return tokens, 201
        except ItemNotFound:
            abort(404, 'User not found')
        except IncorrectPassword:
            abort(401, 'Incorrect password')

    def put(self):
        try:
            refresh_token = request.json.get('refresh_token')
            if not refresh_token:
                abort(400, 'Not valid data passed')

            tokens = auth_service.approve_token(refresh_token)
            return tokens, 201

        except InvalidToken:
            abort(401, 'Invalid token passed')

