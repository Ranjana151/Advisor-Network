"""
This file is responsible for the jwt token decoding
"""


import jwt
import json
import datetime
import os

def decode_auth_token(auth_token):
    """
        Decodes the auth token
        return String
    """
    try:
        # todo save the key in lov table or env variable
        payload = jwt.decode(auth_token,
        "kjdkfhdjkhfkjlkj49873",
        algorithms=["HS256"])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return {"error": 'Token expired. Please log in again.', "code": 401}

    except jwt.InvalidTokenError:
        return {"error": "Invalid token. Please log in again.", "code": 403}
