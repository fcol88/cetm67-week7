"""
RESTful API for Week 7 of CETM67
"""

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import uuid

app = Flask(__name__)
api = Api(app)

version = "1.0.0.0"

tasks = {}

## Require a task to be specified
AddTask_Post_Args = reqparse.RequestParser()
AddTask_Post_Args.add_argument("task", type=str, help="A description of a task", required=True)
AddTask_Post_Args.add_argument("completed", type=bool, help="Describes whether the task has been completed", required=True)

## Route to return API version ##
class GetVersion(Resource):
    def get(self):
        return version

class AddTask(Resource):
    def post(self):
        args = AddTask_Post_Args.parse_args()
        id = str(uuid.uuid4())
        tasks[id] = args
        print(tasks)
        return tasks[id]

api.add_resource(GetVersion, '/version')
api.add_resource(AddTask, '/tasks/add')

if __name__ == "__main__":
    app.run(debug=True)