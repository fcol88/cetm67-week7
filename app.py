"""
RESTful API for Week 7 of CETM67
"""

from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

version = "1.0.0.0"

## Route to return API version ##
class GetVersion(Resource):
    def get(self):
        return version

api.add_resource(GetVersion, '/version')

if __name__ == "__main__":
    app.run(debug=True)