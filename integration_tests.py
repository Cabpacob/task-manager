import requests


endpoint = 'http://localhost:8000/'


def get_response(path):
    response = requests.get(f'{endpoint}{path}')

    assert response.status_code == 200

    return response.text


def post_response(path, data):
    response = requests.post(f'{endpoint}{path}', json=data)

    assert response.status_code == 200

    return response.text


def delete_response(path):
    response = requests.delete(f'{endpoint}{path}')

    assert response.status_code == 200

    return response.text


def test_add_tasks():
    post_response('register-task', {'task_name': 'Do homework', 'progress': 0.9})
    post_response('register-task', {'task_name': 'Feed the cat', 'progress': 1})
    post_response('register-task', {'task_name': 'Make a coffee', 'progress': 0})


def test_get_work():
    post_response('register-task', {'task_name': 'Do homework', 'progress': 0.9})
    post_response('register-task', {'task_name': 'Feed the cat', 'progress': 1})

    get_response('tasks')

    post_response('register-task', {'task_name': 'Make a coffee', 'progress': 0})

    get_response('tasks')


def test_delete_tasks():
    post_response('register-task', {'task_name': 'Do homework', 'progress': 0.9})
    post_response('register-task', {'task_name': 'Feed the cat', 'progress': 1})

    get_response('tasks')

    delete_response('clear-tasks')

    post_response('register-task', {'task_name': 'Make a coffee', 'progress': 0})

    get_response('tasks')

    delete_response('clear-tasks')
    delete_response('clear-tasks')
