from flask import Flask
from flask_restful import Api

from resources.gogogo import Gogogo

app = Flask(__name__)
api = Api(app)

api.add_resource(Gogogo, "/gogogo")

if __name__ == "__main__":
    app.run()