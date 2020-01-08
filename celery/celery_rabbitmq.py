from random import shuffle

from celery import Celery

app = Celery('tasks',
             broker='amqp://guest:guest@localhost:5672',
             backend='amqp://guest:guest@localhost:5672',
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


if __name__ == '__main__':
    app.worker_main()
