import uuid
import pytz

from flask_jwt_extended import get_jwt_identity
from api.todo.model import TodoModel
from http import HTTPStatus
from datetime import datetime
from api.helper.error_handler import APIException

kst = pytz.timezone('Asia/Seoul')

def get_list():
    """model을 사용한 할 일 리스트 조회"""

    try:
        filter_condition = TodoModel.email == get_jwt_identity()
        todos = [todo.to_simple_dict() for todo in TodoModel.scan(filter_condition)]
        
        return {
            'status': HTTPStatus.OK,
            'message': '조회 성공',
            'data': todos
        }
    except Exception as e:
        raise APIException(HTTPStatus.INTERNAL_SERVER_ERROR, str(e))


def create(data):
    """model을 사용한 create"""

    try:
        now = datetime.now(kst).strftime('%Y-%m-%d %H:%M')
        
        todo = TodoModel(
            todo_id=str(uuid.uuid4()),
            email=get_jwt_identity(),
            todo=data.get('todo'),
            created=now,
            state=False
        )
        
        todo.save()
        return {
            'status': HTTPStatus.CREATED,
            'message': '생성 성공',
            'data': todo.to_simple_dict()
        }
    except Exception as e:
        raise APIException(HTTPStatus.INTERNAL_SERVER_ERROR, str(e))

def get_item(todo_id):
    """model을 사용한 할 일 조회"""
    print(f'[service] get_item ::: todo_id => {todo_id}')

    todo = next(TodoModel.query(todo_id), None)
    print(f'[service] get_item ::: todo => {todo}')

    if todo is not None:
        return {
            'status': HTTPStatus.OK,
            'message': '할일 조회 성공.',
            'data': todo.to_simple_dict()
        }
    else:
        return {
            'status': HTTPStatus.NO_CONTENT,
            'message': '일치하는 할일이 없습니다.',
            'data': None
        }

def update(todo_id, data):
    """model을 사용한 할 일 수정"""
    print(f'[service] update ::: todo_id => {todo_id}')
    print(f'[service] update ::: data => {data}')

    todo = next(TodoModel.query(todo_id), None)

    if todo.email != get_jwt_identity():
        return {
            'status': HTTPStatus.UNAUTHORIZED,
            'message': '본인이 생성한 할 일만 수정할 수 있습니다.',
            'data': None
        }

    if todo is None:
        return {
            'status': HTTPStatus.NO_CONTENT,
            'message': '수정할 대상이 없습니다.',
            'data': None
        }

    upd_todo = TodoModel(
        todo_id=todo.todo_id,
        email=todo.email,
        todo=data.get('todo'),
        state=data.get('state'),
        created=todo.created
    )

    save_response = upd_todo.save()
    print(f'[service] update ::: save_response: {save_response}')

    return {
        'status': HTTPStatus.OK,
        'message': '할일 수정 성공.',
        'data': upd_todo.to_simple_dict()
    }


def delete(todo_id):
    """model을 사용한 할 일 삭제"""
    print(f'[service] delete ::: todo_id => {todo_id}')

    sel_todo = next(TodoModel.query(todo_id), None)
    print(f'[service] delete ::: sel_todo: {sel_todo}')

    if sel_todo.email != get_jwt_identity():
        return {
            'status': HTTPStatus.UNAUTHORIZED,
            'message': '본인이 생성한 할 일만 삭제할 수 있습니다.',
            'data': None
        }

    if sel_todo is None:
        return {
            'status': HTTPStatus.NO_CONTENT,
            'message': '삭제 대상을 찾을 수 없습니다.',
            'data': None
        }

    delete_response = sel_todo.delete()
    print(f'[service] delete ::: delete_response: {delete_response}')

    return {
        'status': HTTPStatus.OK,
        'message': '할일 삭제 성공.',
        'data': None
    }