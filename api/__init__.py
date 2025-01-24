from flask import Flask
from flask_restx import Api
from api.user import controllers, user_api

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

    return app