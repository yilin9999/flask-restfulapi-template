from flask_restful import Resource
from flask import request
from models.schema.user import UserSchema
from models.user import UserModel

user_schema = UserSchema(many=False)


class User (Resource):

    def get(self, name):
        user = UserModel.get_user(name)
        if not user:
            return {
                'message': 'username not exist!'
            }, 403
        return {
            'message': '',
            'user': user_schema.dump(user)
        }

    def post(self, name):
        
        #try: 
        result = user_schema.load(request.json)
    # print(result)
    # print(type(result))

    # if len(result.errors) > 0:
    #     return result.errors, 433

        user = UserModel(name, result['email'], result['password'])
        user.add_user()
        return {
            'message': 'Insert user success',
            'user': user_schema.dump(user)
        }
        # except Exception as err:
        #     return {
        #         'message': str(err),
        #     }, 443
            

    def put(self, name):
        result = user_schema.load(get_param())
        # if len(result.errors) > 0:
        #     return result.errors, 433

        user = UserModel.get_user(name)
        if not user:
            return {
                'message': 'username not exist!'
            }, 403
        user.email = result['email']
        user.password = result['password']
        user.update_user()
        return {
            'message': 'Update user success',
            'user': user_schema.dump(user)
        }

    def delete(self, name):
        UserModel.delete_user(name)
        return {
            'message': 'Delete done!'
        }


class Users(Resource):
    def get(self):
        # print(UserModel.get_all_user())
        # print(type(UserModel.get_all_user()))
        return {
            'message': '',
            'users': user_schema.dump(UserModel.get_all_user())
        }
