import datetime
from flask import current_app
from flask_jwt_extended import create_access_token, get_jwt_identity

def util_jwt_create_access_token(identity):
    current_app.config['JWT_SECRET_KEY'] = 'your_default_secret_key'
    expires_delta = datetime.timedelta(seconds=60 * 60 * 24)  # 24 hours
    access_token = create_access_token(identity, expires_delta)
    return access_token