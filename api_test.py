"""
Test file for API
"""

import requests

BASE_URL = "http://127.0.0.1:5000/"

def print_response(response):
    print(response.status_code,
     f"\n{response.json()}")

print("Checking version...")
response = requests.get(BASE_URL + "version")
print_response(response)

print("Creating task...")
response = requests.post(BASE_URL + "tasks/add", json = {"description" : "Test my API", "completed" : False})
print_response(response)
id = response.json()['taskId']

print("Getting task list...")
response = requests.get(BASE_URL + "tasks/")
print_response(response)
## expected that one task will be displayed as incomplete

print("Updating task...")
response = requests.patch(BASE_URL + "tasks/update/" + id, json = {"completed":True})
print_response(response)

print("Validating that task list is updated...")
response = requests.get(BASE_URL + "tasks/")
print_response(response)
## expected that one task will be displayed as complete

print("Downloading image...")
response = requests.get(BASE_URL + "downloadimage")
print_response(response)
## expected that image is downloaded - may return false without credentials though

print("Unsuccessful task request")
response = requests.post(BASE_URL + "tasks/add")
print_response(response)

print("Unsuccessful task patch")
response = requests.patch(BASE_URL + "tasks/update/", json = {"completed":True})

print(BASE_URL + "Wrong method post")
response = requests.post(BASE_URL + "tasks/")