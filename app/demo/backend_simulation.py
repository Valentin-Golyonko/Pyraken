from demo.tasks import add, mul, args_sum, hello, my_sort


def check_celery_tasks():
    print(add.name)
    a1 = add.delay(3, -2)
    print(a1.get())


def tasks_for_one_cpu():
    for i in range(50):
        my_sort(5)


def task_for_four_cpus():
    done_tasks = []
    for i in range(50):
        done_tasks.append(my_sort.delay(5))

    print('all tasks sent')

    while done_tasks:
        for dt in done_tasks:
            if dt.state != 'PENDING':
                done_tasks.remove(dt)

    print('all tasks done')

