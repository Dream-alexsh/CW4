from datetime import datetime, timedelta

import jwt
from flask import current_app, request
from flask_restx import abort

from project.exceptions import InvalidToken, IncorrectPassword
from project.service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, user, is_refresh=False):

        email_passed = user.get('email')
        password_passed = user.get('password')
        user = self.user_service.get_by_email(email_passed)

        if not is_refresh:
            password_is_correct = self.user_service.compare_password(user.password, password_passed)
            if not password_is_correct:
                raise IncorrectPassword

        payload = {
            'email': user.email,
            'exp': datetime.utcnow() + timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
        }

        access_token = jwt.encode(
            payload=payload,
            key=current_app.config['SECRET_KEY'],
            algorithm=current_app.config['JWT_ALGORITHM'],
        )

        payload['exp'] = datetime.utcnow() + timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])

        refresh_token = jwt.encode(
            payload=payload,
            key=current_app.config['SECRET_KEY'],
            algorithm=current_app.config['JWT_ALGORITHM'],
        )

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def get_email_from_token(self, token: str):
        try:
            data = jwt.decode(token,
                              current_app.config.get('SECRET_KEY'),
                              algorithms=[current_app.config.get('JWT_ALGORITHM')])
            email = data.get('email')
            return email
        except Exception:
            raise InvalidToken

    def approve_token(self, refresh_token: str):
        users = {
            'email': self.get_email_from_token(refresh_token),
            'password': None
        }
        new_tokens = self.generate_tokens(users, is_refresh=True)
        return new_tokens

    @staticmethod
    def auth_required(func):

        def wrapper(*args, **kwargs):
            if 'Authorization' not in request.headers:
                abort(401, 'No authorization data passed')

            data = request.headers['Authorization']
            token = data.split("Bearer ")[-1]

            try:
                jwt.decode(token, current_app.config.get('SECRET_KEY'),
                           algorithms=[current_app.config.get('JWT_ALGORITHM')])
            except Exception as e:
                abort(401, f'JWT decode error {e}')

            return func(*args, **kwargs)

        return wrapper
