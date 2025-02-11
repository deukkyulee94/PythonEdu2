from flask_restx import Namespace, fields
from api.user import email_field

todo_api = Namespace(
    name='todo',
    path='/todos',
    description='할 일 관련된 API 모음입니다.'
)

todo_id_field = fields.String(
    required=True,
    title='todo 고유 아이디',
    description='todo 생성 시 자동 생성 됩니다.',
    example='1'
)

todo_field = fields.String(
    required=True,
    title='할 일',
    description='할 일 내용',
    example='장보기'
)
state_field = fields.Boolean(
    required=True,
    title='완료 여부',
    description='완료 여부',
    example=False
)

create_request = todo_api.model('create_request', {
    'todo': todo_field
})

read_list_request = todo_api.model('read_request', {
    'email': email_field
})

update_request = todo_api.model('update_request', {
    'todo': todo_field,
    'state': state_field
})

response = todo_api.model('todo_response_model', {
    'status': fields.Raw(required=True, description='응답 상태'),
    'message': fields.String(required=True, description='응답 메시지'),
    'data': fields.Raw(drequired=True, description='응답 데이터'),
})