# To Do List Server Mock
Mock server for automation job candidates.

- Server implements RESTful API
- All API responses are formatted in JSON
- The server will be answering to requests on port 5000 (http://localhost:5000)


#### HTTP status codes
If you're unfamiliar with the HTTP status code, you may find this information useful: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

## Environment Prerequisites #
- Python 2.7.x: https://www.python.org/downloads/release/python-2712/
- Pip 8.1 or above: https://pip.pypa.io/en/stable/installing/


## Installation #
As best practice (not mandatory), we recommend installing virtualenv and virtualenvwrapper.

- Installing virtualenv: https://virtualenv.pypa.io/en/latest/installation/

- Installing virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/install.html

Then, to install project prerequisites, inside the project root, run:
```
pip install .
```
### Run the server mock
#### Windows
```buildoutcfg
C:\path\to\app>set FLASK_APP=server.py
C:\path\to\app>flask run
```

#### Linux
```buildoutcfg
export FLASK_APP=server.py
flask run
```


## Authentication
Authentication is *not* required.


## API Endpoints
Following is the complete list of endpoints to work against.


#### Listing tasks
Description: Listing tasks  
Usage: GET /tasks  
Produces: application/json

Sample response:
```buildoutcfg
{}
```
---
#### Get task
Description: Get a single task  
Usage: GET /tasks/<task_id>  
Produces: application/json  

##### parameters
- <task_id>: task id. Can be retrieved when creating a new task, or when 
listing all tasks.

Sample response:
```buildoutcfg
{
  "task": "add task",
  "completed": false
}
```
---
#### Create task
Description: Create a task  
Usage: POST /tasks/<task_id> 
Produces: application/json  

##### parameters
- <task_id>: task id. Can be retrieved when creating a new task, or when 
listing all tasks.
##### request body
JSON formatted object with attributes:
- task: task title
- completed: (boolean) whether task is completed

Sample request:
```buildoutcfg
{
  "task": "add task",
  "completed": false
}
```

Sample response:
```buildoutcfg
{
  "task_id": "1234",
}
```
---
#### Modify task
Description: Modifies an existing task   
Usage: PUT /tasks/<task_id>  
Produces: application/json 

##### parameters
- <task_id>: task id. Can be retrieved when creating a new task, or when 
listing all tasks.

Sample request:
```buildoutcfg
{
  "task": "add task",
  "completed": false
}
```

Sample response:
```buildoutcfg
{
  "task_id": "1234",
}
```
---
#### Mark task completed
Description: Mark an existing task as completed  
Usage: POST /tasks/<task_id>/completed  
Produces: application/json 

##### parameters
- <task_id>: task id. Can be retrieved when creating a new task, or when 
listing all tasks. 

Sample response:
```buildoutcfg
{}
```

---
#### Mark task incomplete
Description: Mark an existing task as incomplete    
Usage: POST /tasks/<task_id>/completed  
Produces: application/json 

##### parameters
- <task_id>: task id. Can be retrieved when creating a new task, or when 
listing all tasks.

Sample response:
```buildoutcfg
{}
```

---
#### Delete a task
Description: Delete an existing task     
Usage: DELETE /tasks/<task_id>  
Produces: application/json 

##### parameters
- <task_id>: task id. Can be retrieved when creating a new task, or when 
listing all tasks.

Sample response:
```buildoutcfg
{}
```