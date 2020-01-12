from flask_restful import Resource

class Gogogo(Resource):
    def get(self):
        return {
            'message': 'ready to gogogo'
        }, 200