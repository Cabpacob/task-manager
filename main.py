from fastapi import FastAPI
from starlette import status
from starlette.responses import Response
from typing import Optional
from pydantic import BaseModel
import time

app = FastAPI()

@app.get('/api/{version}')
def get_api_version(version):
    return f'Your api version = {version}'

class TaskManager:
    __tasks = []

    def add_task(self, task_name, progress, spent_hours=None):
        self.__tasks.append((task_name.strip(), progress, spent_hours, time.time()))

    def get_work(self):
        def task_to_string(task):
            result = f'You did task {task[0]} by {int(task[1] * 100)}% at {time.ctime(task[3])}'
            if task[2] is not None:
                result += f' and spent {task[2]} hours'
            return result

        return '\n'.join(map(task_to_string, self.__tasks))



task_manager = TaskManager()


@app.get('/tasks')
def get_tasks():
    return task_manager.get_work()


class TaskProgress(BaseModel):
    task_name: str
    progress: float
    spent_hours: Optional[float] = None


@app.post('/register-task')
def get_strange_data(data: TaskProgress):
    if data.progress < 0 or data.progress > 1:
        return Response('Wrong progress, it must be betwen 0 and 1', status_code=status.HTTP_400_BAD_REQUEST)

    if data.spent_hours is not None and data.spent_hours <= 0:
        return Response('Wrong spent_hours, it must be greater than 0', status_code=status.HTTP_400_BAD_REQUEST)

    task_manager.add_task(data.task_name, data.progress, data.spent_hours)
    return Response('Task successfully added', status_code=status.HTTP_200_OK)
