from flask_jwt_extended import jwt_required
from flask_restx import Resource
from api.todo import todo_api, create_request, update_request, response
from api.todo.service import create, get_list, get_item, update, delete

@todo_api.route('/')
class Todo(Resource):

    @jwt_required()
    @todo_api.expect()
    @todo_api.marshal_with(response)
    def get(self):
        return get_list()

    @jwt_required()
    @todo_api.expect(create_request)
    @todo_api.marshal_with(response)
    def post(self):
        return create(todo_api.payload)

@todo_api.route('/<string:todo_id>')
class TodoDetail(Resource):

    @jwt_required()
    @todo_api.marshal_with(response)
    def get(self, todo_id):
        return get_item(todo_id)

    @jwt_required()
    @todo_api.expect(update_request)
    @todo_api.marshal_with(response)
    def put(self, todo_id):
        return update(todo_id, todo_api.payload)

    @jwt_required()
    @todo_api.expect()
    @todo_api.marshal_with(response)
    def delete(self, todo_id):
        return delete(todo_id)