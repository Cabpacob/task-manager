from lib import TaskManager
import pytest
import random


def must_except(function):
    try:
        function()
    except:
        pass
    else:
        assert False, 'Function must except'


def test_task_manager_pipeline():
    tm = TaskManager()

    tm.add_task('Buy a bread', 0, timestamp=False)
    tm.add_task('Turn off the iron', 1, timestamp=False)

    answer = [
        'You did task Buy a bread by 0%',
        'You did task Turn off the iron by 100%'
    ]

    assert tm.size() == 2
    assert tm.get_task_progress('Buy a bread') == 0
    assert tm.get_work() == '\n'.join(answer)

    tm.clear()

    assert tm.size() == 0
    must_except(lambda: tm.get_task_progress('Buy a bread'))
    assert tm.get_work() == ''

    tm.add_task('Buy a bread', 1, timestamp=False)

    answer = [
        'You did task Buy a bread by 100%',
    ]

    assert tm.size() == 1
    assert tm.get_task_progress('Buy a bread') == 1
    assert tm.get_work() == '\n'.join(answer)

    tm.clear()

    tm.add_task('Buy a bread', 1, timestamp=False)
    tm.add_task('Buy a bread', 0.5, timestamp=False)

    must_except(lambda: tm.get_task_progress('But a bread'))


def test_performance_with_clear():
    tm = TaskManager()

    N = 5 * 100000

    def add_task():
        size = tm.size()
        tm.add_task(f'Task number {size + 1}', 0.4, 10)

    def get_work():
        tm.get_work()

    def get_task_progress():
        size = tm.size()

        if size == 0:
            must_except(lambda: tm.get_task_progress('Task number 0'))
        else:
            tm.get_task_progress(f'Task number {random.randint(1, size)}')

    def clear():
        tm.clear()

    command_list = [
        add_task,
        get_work,
        get_task_progress,
        clear
    ]

    for _ in range(N):
        command_number = len(command_list)
        command = command_list[random.randint(0, command_number - 1)]
        command()


def test_performance_without_clear():
    tm = TaskManager()

    N = 5 * 1000

    def add_task():
        size = tm.size()
        tm.add_task(f'Task number {size + 1}', 0.4, 10)

    def get_work():
        tm.get_work()

    def get_task_progress():
        size = tm.size()

        if size == 0:
            must_except(lambda: tm.get_task_progress('Task number 0'))
        else:
            tm.get_task_progress(f'Task number {random.randint(1, size)}')

    command_list = [
        add_task,
        get_work,
        get_task_progress,
    ]

    for _ in range(N):
        command_number = len(command_list)
        command = command_list[random.randint(0, command_number - 1)]
        command()
