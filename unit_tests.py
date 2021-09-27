from lib import TaskManager
import pytest


def test_add_task():
    tm = TaskManager()
    tm.add_task('Do homework', 0.7, 2)


@pytest.mark.xfail()
def test_wrong_progress():
    tm = TaskManager()
    tm.add_task('Do homework', -1)


@pytest.mark.xfail()
def test_wrong_spent_hours():
    tm = TaskManager()
    tm.add_task('Do smth', 0.5, 0)


def test_get_work():
    tm = TaskManager()
    tm.add_task('Do homework', 0.8, 2, timestamp=False)
    tm.add_task('Do tests', 0.6, 0.5, timestamp=False)
    tm.add_task('Do something else', 0.2, timestamp=False)

    answer = [
        'You did task Do homework by 80% and spent 2 hours',
        'You did task Do tests by 60% and spent 0.5 hours',
        'You did task Do something else by 20%'
    ]

    assert tm.get_work() == '\n'.join(answer)


def test_get_empty_work():
    tm = TaskManager()
    assert tm.get_work() == ''


def test_get_work_changing():
    tm = TaskManager()
    tm.add_task('Do homework', 0.8, 2, timestamp=False)
    tm.add_task('Do tests', 0.6, 0.5, timestamp=False)

    answer = [
        'You did task Do homework by 80% and spent 2 hours',
        'You did task Do tests by 60% and spent 0.5 hours'
    ]

    assert tm.get_work() == '\n'.join(answer)

    tm.add_task('Do something else', 0.2, timestamp=False)
    answer.append('You did task Do something else by 20%')

    assert tm.get_work() == '\n'.join(answer)


def test_get_progress():
    tm = TaskManager()
    tm.add_task('Do homework', 0.8, 2, timestamp=False)
    tm.add_task('Do tests', 0.6, 0.5, timestamp=False)
    tm.add_task('Do something else', 0.2, timestamp=False)

    assert tm.get_task_progress('Do homework') == 0.8
    assert tm.get_task_progress('Do tests') == 0.6
    assert tm.get_task_progress('Do something else') == 0.2


@pytest.mark.xfail()
def test_get_progress_wrong_task_name():
    tm = TaskManager()

    tm.add_task('Do homework', 0.8, 2, timestamp=False)

    tm.get_task_progress('Feed the cat')


@pytest.mark.xfail()
def test_get_progress_tasks_more_than_one():
    tm = TaskManager()

    tm.add_task('Do homework', 0.8, 2, timestamp=False)
    tm.add_task('Do homework', 0.1, 2, timestamp=False)

    tm.get_task_progress('Do homework')


def test_clear():
    tm = TaskManager()
    tm.clear()

    tm.add_task('Do homework', 0.8, 2, timestamp=False)
    tm.clear()


def test_clear_with_get_progress():
    tm = TaskManager()
    tm.add_task('Do homework', 0.8, 2, timestamp=False)

    assert tm.get_task_progress('Do homework') == 0.8

    tm.clear()

    try:
        tm.get_task_progress('Do homework')
    except:
        pass
    else:
        assert False, 'TaskManager does not cleared'


def test_clear_with_get_work():
    tm = TaskManager()
    tm.add_task('Do homework', 0.8, 2, timestamp=False)
    tm.clear()

    assert tm.get_work() == ''


def test_empty_size():
    tm = TaskManager()

    assert tm.size() == 0


def test_size():
    tm = TaskManager()

    tm.add_task('Do homework', 0.8, 2, timestamp=False)
    tm.add_task('Do homework', 0.1, 2, timestamp=False)
    tm.add_task('Do tests', 0.6, 0.9, timestamp=False)
    tm.add_task('Do something else', 0.2, timestamp=False)

    assert tm.size() == 4

def test_size_with_clear():
    tm = TaskManager()

    tm.add_task('Do homework', 0.8, 2, timestamp=False)
    tm.add_task('Do homework', 0.1, 2, timestamp=False)
    tm.add_task('Do tests', 0.6, 0.9, timestamp=False)
    tm.add_task('Do something else', 0.2, timestamp=False)

    tm.clear()

    assert tm.size() == 0
