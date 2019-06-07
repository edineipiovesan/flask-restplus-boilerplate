from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='User related operations')
    request = api.model('user', {
        'email': fields.String(required=True, description='User email address'),
        'username': fields.String(required=True, description='User username'),
        'password': fields.String(required=True, description='User password')
    })
    response = api.model('user', {
        'email': fields.String(required=True, description='User email address'),
        'username': fields.String(required=True, description='User username'),
        'public_id': fields.String(description='User identifier')
    })



class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
