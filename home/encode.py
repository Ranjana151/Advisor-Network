"""
For encodig of jwt token
"""
import jwt
import datetime
import os


def encode_auth_token(subject, type):
    """
        Generates auth token
        return: String
    """
    try:
        if type == 'login':
            LOGIN_SESSION_TIME = 4
        else:
            LOGIN_SESSION_TIME = 24
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=LOGIN_SESSION_TIME, seconds=0),
            'iat': datetime.datetime.utcnow(),
            'sub': subject
        }

        return jwt.encode(
            payload,
            "kjdkfhdjkhfkjlkj49873",
            algorithm='HS256'
        )

    except Exception as e:
        return e
