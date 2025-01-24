from flask_restx import Resource
from api.user import user_api, signup_request, signin_request, response
from api.user.service import signup, signin

@user_api.route('/signup')
class Signup(Resource):
    @user_api.expect(signup_request)
    @user_api.marshal_with(response)
    def post(self):
        return signup(user_api.payload)

@user_api.route('/signin')
class Signin(Resource):
    @user_api.expect(signin_request)
    @user_api.marshal_with(response)
    def post(self):
        return signin(user_api.payload)
