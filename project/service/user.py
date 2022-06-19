import base64
import hashlib
import hmac

from flask import current_app
from werkzeug.exceptions import MethodNotAllowed

from project.dao.user import UserDAO
from project.exceptions import ItemNotFound, IncorrectPassword, UserAlreadyExists
from project.service.base import BaseService


class UserService(BaseService[UserDAO]):

    def get_by_email(self, email):
        user = self.dao.get_by_email(email)

        if not user:
            raise ItemNotFound
        return user

    def create(self, user_d):
        user = self.dao.get_by_email(user_d.get('email'))
        if user:
            raise UserAlreadyExists

        user_d['password'] = self.hash_password(user_d.get('password'))
        user = self.dao.create(user_d)
        return user

    def update(self, user_d, email):
        self.get_by_email(email)
        if 'password' not in user_d.keys() and 'email' not in user_d.keys():
            self.dao.update(user_d, email)
        else:
            raise MethodNotAllowed

    def update_password(self, user_d, email):

        user = self.get_by_email(email)
        current_password = user_d.get('old_password')
        new_password = user_d.get('new_password')

        if None in [current_password, new_password]:
            raise MethodNotAllowed

        if not self.compare_password(user.password, current_password):
            raise IncorrectPassword

        data = {
            'password': self.hash_password(new_password)
        }
        self.dao.update(data, email)

    def hash_password(self, password: str):
        hash_digest = self.create_hash(password)
        encoded_digest = base64.b64encode(hash_digest)
        return encoded_digest

    def create_hash(self, password: str):
        hash_digest: bytes = hashlib.pbkdf2_hmac(
            current_app.config.get('PWD_HASH_NAME'),
            password.encode('utf-8'),
            current_app.config.get('PWD_HASH_SALT'),
            current_app.config.get('PWD_HASH_ITERATIONS')
        )
        return hash_digest

    def compare_password(self, password_hash: str, password_new: str) -> bool:
        decoded_digest = base64.b64decode(password_hash)
        passed_hash = self.create_hash(password_new)
        is_digest = hmac.compare_digest(decoded_digest, passed_hash)
        return is_digest


