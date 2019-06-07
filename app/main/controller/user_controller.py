from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ..util.dto import UserDto

api = UserDto.api
user_resquest = UserDto.request
user_response = UserDto.response


@api.route('/')
class UserList(Resource):
    @admin_token_required
    @api.doc('list_of_registereduser_resquests')
    @api.marshal_list_with(user_response, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(user_resquest, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(user_response)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
