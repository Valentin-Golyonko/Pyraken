from __future__ import absolute_import, unicode_literals

from random import shuffle

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def args_sum(*args):
    return sum(*args)


@shared_task
def hello(word):
    return "hello " + word


@shared_task
def my_sort(x):
    arr = list(range(10 ** x))
    shuffle(arr)
    sorted(arr)
    return 'done'
