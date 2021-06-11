# CETM67 Week 7 Flask API



This is a small API with several endpoints and an integration with S3.



## Endpoints



### /version

Returns the version of the API (1.0.0.0)



### /tasks/add

A POST endpoint which accepts a JSON payload of:

- "description" : "a string describing the task"
- "completed": "a boolean describing whether the task has been completed"



### /tasks/update/{id}



A PATCH endpoint - the ID provided from the /add endpoint must be added here in order to update the correct task. Accepts a JSON payload of:

- "completed" : "a boolean describing whether the task has been completed"



### /tasks/

A GET endpoint - returns a list of all tasks including their IDs, descriptions and completion status



### /downloadimage



A GET endpoint - connects to S3 and downloads an image file from a public S3 bucket, then returns a status message confirming whether it was successful.