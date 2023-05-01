import base64
import calendar
import datetime
import hashlib
import jwt
from flask import request, abort

from config import Config

def generate_tokens(data, is_refresh=False):
    # Токен доступа на 30 мин
    secret = Config.JWT_SECRET
    algo = Config.JWT_ALGO
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, secret, algorithm=algo)

    # Токен доступа на 130 дней
    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    data["exp"] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(data, secret, algorithm=Config.JWT_ALGO)
    return {"access_token": access_token, "refresh_token": refresh_token}

def generate_pw_hash(pw):
    hash_digest = hashlib.pbkdf2_hmac(
        'sha256',
        pw.encode('utf-8'),
        Config.PWD_SALT,
        Config.PWD_ITERATIONS
    )
    return base64.b64encode(hash_digest)


def auth_required(func):
    def wrapper(*args, **kwarg):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGO])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwarg)
    return wrapper