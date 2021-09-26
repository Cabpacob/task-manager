from typing import Optional
from pydantic import BaseModel


class TaskManager:
    __tasks = []

    def add_task(self, task_name, progress, spent_hours=None):
        class Task:
            def __init__(self, name, progress, spent_hours, current_time):
                assert progress >= 0 and progress <= 1, 'Wrong progress, it must be betwen 0 and 1'
                assert spent_hours is None or data.spent_hours > 0, 'Wrong spent_hours, it must be greater than 0'

                self.name = name.strip()
                self.progress = progress
                self.spent_hours = spent_hours
                self.current_time = current_time

            def __str__(self):
                result = f'You did task {self.name} by {int(self.progress * 100)}% at {time.ctime(self.current_time)}'
                if self.spent_hours is not None:
                    result += f' and spent {self.spent_hours} hours'
                return result


        self.__tasks.append(Task(task_name, progress, spent_hours, time.time()))

    def get_work(self):
        return '\n'.join(map(str, self.__tasks))


class TaskProgress(BaseModel):
    task_name: str
    progress: float
    spent_hours: Optional[float] = None

