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


@app.get('/tasks')
def get_tasks():
    return task_manager.get_work()


@app.post('/register-task')
def get_task_progress(data: TaskProgress):
    try:
        task_manager.add_task(data.task_name, data.progress, data.spent_hours)
    except Exception as e:
        return Response(f'Raised exception {e}', status_code=status.HTTP_400_BAD_REQUEST)
    return Response('Task successfully added', status_code=status.HTTP_200_OK)
