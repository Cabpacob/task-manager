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
    if data.progress < 0 or data.progress > 1:
        return Response('Wrong progress, it must be betwen 0 and 1', status_code=status.HTTP_400_BAD_REQUEST)

    if data.spent_hours is not None and data.spent_hours <= 0:
        return Response('Wrong spent_hours, it must be greater than 0', status_code=status.HTTP_400_BAD_REQUEST)

    task_manager.add_task(data.task_name, data.progress, data.spent_hours)
    return Response('Task successfully added', status_code=status.HTTP_200_OK)
