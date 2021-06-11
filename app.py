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
AddTask_Post_Args.add_argument("description", type=str, help="A description of a task", required=True)
AddTask_Post_Args.add_argument("completed", type=bool, help="Provide a value on whether the task has been completed: True or False", required=True)

UpdateTask_Patch_Args = reqparse.RequestParser()
UpdateTask_Patch_Args.add_argument("completed", type=bool, help="A value to update the task status to", required=True)

## Route to return API version ##
class GetVersion(Resource):
    def get(self):
        return version

class AddTask(Resource):
    def post(self):
        args = AddTask_Post_Args.parse_args()
        id = str(uuid.uuid4())
        tasks[id] = args
        return {"taskId": id, "task": tasks[id]}

class UpdateTask(Resource):
    def patch(self, id):
        args = UpdateTask_Patch_Args.parse_args()
        tasks[id]['completed'] = args['completed']
        return {"taskId" : id, "task" : tasks[id]}

class ListTasks(Resource):
    def get(self):
        return tasks

api.add_resource(GetVersion, '/version')
api.add_resource(AddTask, '/tasks/add')
api.add_resource(UpdateTask, '/tasks/update/<string:id>')
api.add_resource(ListTasks, '/tasks/')

if __name__ == "__main__":
    app.run(debug=True)