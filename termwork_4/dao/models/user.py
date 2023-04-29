import base64
import hashlib
import hmac

from config import Config
from marshmallow import Schema, fields

from setup_db import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre = db.Column(db.String(255))

    def compare_password(self, pwd_from_req) ->bool:
        pwdhash_in_db = self.password
        decoded_pwdhash_db = base64.b64decode(pwdhash_in_db)
        new_hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            pwd_from_req.encode(),
            Config.PWD_SALT,
            Config.PWD_ITERATIONS
        )
        return hmac.compare_digest(decoded_pwdhash_db, new_hash_digest)


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String()
    password = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre = fields.String()