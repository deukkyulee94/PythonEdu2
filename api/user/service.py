from api.user.model import UserModel
from http import HTTPStatus

def signup(data):
    """model을 사용한 signup"""

    print(f'[service] signup ::: payload => {data}')
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')

    user = UserModel.query(email)

    first_data = next(user, None)

    if first_data is None:
        user = UserModel(email=email, name=name, password=password)
        user.save()
        print(f'[service] signup ::: user.to_simple_dict() => {user.to_simple_dict()}')
        return {
            'status': HTTPStatus.OK,
            'message': '회원가입 성공.',
            'data': user.to_simple_dict()
        }
    else:
        return {
            'status': HTTPStatus.CONFLICT,
            'message': '회원가입 실패, 이미 존재하는 유저입니다.',
            'data': None
        }

def signin(data):
    '''model을 사용한 signin'''

    # print(f'[service] signin: {data}')
    email = data.get('email')
    password = data.get('password')

    filter_condition = None
    filter_condition &= (UserModel.email == email)
    filter_condition &= (UserModel.password == password)
    user = UserModel.scan(filter_condition)

    if len(list(user)) == 1:
        access_token = util_jwt_create_access_token(identity=email)
        return {'message': '로그인 성공', 'jwt': access_token}, HTTPStatus.OK
    else:
        return {'message': '로그인 실패'}, HTTPStatus.UNAUTHORIZED

