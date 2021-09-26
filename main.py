from fastapi import FastAPI
from starlette import status
from starlette.responses import Response
from lib import TaskManager, TaskProgress
import time


app = FastAPI()
task_manager = TaskManager()


@app.get('/api/{version}')
def get_api_version(version):
    return f'Your api version = {version}'


def get_work():
    return task_manager.get_work()


@app.get('/tasks')
def get_tasks():
    return get_work()


def add_task(task):
    task_manager.add_task(task.task_name, task.progress, task.spent_hours)


@app.post('/register-task')
def post_register_task(data: TaskProgress):
    try:
        add_task(data)
    except Exception as e:
        return Response(f'Raised exception {e}', status_code=status.HTTP_400_BAD_REQUEST)
    return Response('Task successfully added', status_code=status.HTTP_200_OK)


def task_progress(task_name):
    progress = None
    try:
        progress = task_manager.get_task_progress(task_name)
    except Exception as e:
        return 'Wrong task_name'
    return f'Task progress = {progress}'


@app.get('/task/{name}')
def get_task_progress(name):
    return task_progress(name)


@app.delete('/clear-tasks')
def delete_tasks():
    task_manager.clear()
