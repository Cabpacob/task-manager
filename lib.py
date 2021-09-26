from typing import Optional
from pydantic import BaseModel


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


class TaskProgress(BaseModel):
    task_name: str
    progress: float
    spent_hours: Optional[float] = None

