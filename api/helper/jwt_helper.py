import datetime
from flask import current_app
from flask_jwt_extended import create_access_token

def util_jwt_create_access_token(identity):
    current_app.config['JWT_SECRET_KEY'] = '\xf38\xd1\xa6=\xb5\xf0Q\x00\x15\xa9x\xd5\xf8\x04\xcf'
    expires_delta = datetime.timedelta(seconds=60 * 60 * 24)  # 24 hours
    access_token = create_access_token(identity, expires_delta)
    return access_token