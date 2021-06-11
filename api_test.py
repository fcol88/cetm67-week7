"""
Test file for API
"""

import requests

BASE_URL = "http://127.0.0.1:5000/"

def print_response(response):
    print(response.status_code,
     f"\n{response.json()}")

response = requests.post(BASE_URL + "/tasks/add", json = {"description" : "Add a task", "completed" : False})
print_response(response)
id = response.json()['taskId']

response = requests.patch(BASE_URL + "tasks/update/" + id, json = {"completed":True})
print_response(response)