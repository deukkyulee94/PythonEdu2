from flask import jsonify
from http import HTTPStatus

class APIException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

def handle_api_exception(error):
    response = {
        'status': error.status_code,
        'message': error.message,
        'data': None
    }
    return jsonify(response), error.status_code 