from flask_restx import Namespace, fields

user_api = Namespace(
    name='user',
    path='/users',
    description='사용자와 관련된 API 모음입니다.'
)

email_field = fields.String(
    required=True,
    title='이메일',
    description='아이디로 사용됩니다.',
    example='test@gmail.com',
    pattern="([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
)
name_field = fields.String(
    required=True,
    title='사용자 이름',
    description='사용자 이름',
    example='Evan'
)
password_field = fields.String(
    required=True,
    title='비밀번호',
    description='4자리 이상 입력해야 합니다.',
    example='1234',
    min_length=4
)

signup_request = user_api.model('signupRequest', {
    'email': email_field,
    'name': name_field,
    'password': password_field
})

signin_request = user_api.model('loginRequest', {
    'email': email_field,
    'password': password_field
})

response = user_api.model('responseModel', {
    'status': fields.Raw(required=True, description='응답 상태'),
    'message': fields.String(required=True, description='응답 메시지'),
    'data': fields.Raw(drequired=True, description='응답 데이터'),
})