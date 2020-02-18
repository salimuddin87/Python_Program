from json import dumps
from werkzeug.exceptions import BadRequest
from flask import (
    Flask,
    Response,
    request
)


from utils import get_random_id


app = Flask(__name__)

tasks = {
    get_random_id(): {
        "task": "write server mock",
        "completed": True
    },
    get_random_id(): {
        "task": "say Hello",
        "completed": False
    }
}


@app.route(
    '/tasks',
    methods=['GET']
)
def list_tasks():
    li = [
        {
            "id": task_id,
            "task": values["task"],
            "completed": values["completed"]
        } for task_id, values in tasks.iteritems()
    ]
    return Response(
        dumps(li),
        mimetype='application/json'
    )


@app.route(
    '/tasks/<task_id>',
    methods=['GET']
)
def get_task(task_id):
    if task_id in tasks:
        return Response(
            dumps(tasks[task_id]),
            mimetype='application/json'
        )
    return Response(
        '{}',
        mimetype='application/json'
    ), 404


@app.route(
    '/tasks',
    methods=['POST']
)
def create_task():
    try:
        data = request.get_json()
    except BadRequest:
        return Response(
            '{}',
            mimetype='application/json'
        ), 400
    required_keys = [
        'task',
        'completed'
    ]
    for required_key in required_keys:
        if required_key not in data:
            return Response(
                '{}',
                mimetype='application/json'
            ), 400
    task_id = get_random_id()
    tasks[task_id] = {
        'task': data['task'],
        'completed': data['completed']
    }
    response = {
        'task_id': task_id
    }
    return Response(
        dumps(response),
        mimetype='application/json'
    )


@app.route(
    '/tasks/<task_id>/completed',
    methods=['POST']
)
def mark_task_completed(task_id):
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        return Response(
            '{}',
            mimetype='application/json'
        )
    return Response(
        '{}',
        mimetype='application/json'
    ), 404


@app.route(
    '/tasks/<task_id>/incomplete',
    methods=['POST']
)
def mark_task_incomplete(task_id):
    if task_id in tasks:
        tasks[task_id]["completed"] = False
        return Response(
            '{}',
            mimetype='application/json'
        )
    return Response(
        '{}',
        mimetype='application/json'
    ), 404


@app.route(
    '/tasks/<task_id>',
    methods=['DELETE']
)
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        response = {
            "task_id": task_id
        }
        return Response(
            dumps(response),
            mimetype='application/json'
        )
    return Response(
        '{}',
        mimetype='application/json'
    ), 404


@app.route(
    '/tasks/<task_id>',
    methods=['PUT']
)
def modify_task(task_id):
    if task_id not in tasks:
        return Response(
            '{}',
            mimetype='application/json'
        ), 404

    try:
        data = request.get_json()
    except BadRequest:
        return Response(
            '{}',
            mimetype='application/json'
        ), 400
    required_keys = [
        'task',
        'completed'
    ]
    for required_key in required_keys:
        if required_key not in data:
            return Response(
                '{}',
                mimetype='application/json'
            ), 400
    tasks[task_id] = {
        'task': data['task'],
        'completed': data['completed']
    }
    response = {
        'task_id': task_id
    }
    return Response(
        dumps(response),
        mimetype='application/json'
    )


if __name__ == "__main__":
    pass