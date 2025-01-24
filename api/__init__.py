from flask import Flask
from flask_restx import Api
from api.user import controller, user_api
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)

    # for zappa health check
    app.add_url_rule('/', endpoint='ping', view_func=lambda: 'Pong!')

    # for swagger
    authorizations = {
        'user_token': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'JWT for user'
        },
    }
    api = Api(app,
              authorizations=authorizations,
              security='user_token',
              doc='/swagger',
              title='Evan-flask-edu',
              version='1.0',
              description='Flask-Restx를 이용한 백엔드 API')

    # add namespace
    api.add_namespace(user_api)

    # JWT Config
    jwt = JWTManager()
    jwt.init_app(app)

    return app