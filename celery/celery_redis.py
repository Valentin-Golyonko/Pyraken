from random import shuffle

from celery import Celery

app = Celery('tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             )


@app.task
def test_task():
    return "test task is here!"


@app.task
def add(x, y):
    return x + y


@app.task
def hello(word):
    return "hello " + word


@app.task
def my_sort(x):
    arr = list(range(10 ** x))
    shuffle(arr)
    sorted(arr)
    return 'done'
