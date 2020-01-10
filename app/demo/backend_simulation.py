import json
from time import perf_counter

from demo.tasks import mul, my_sort


def check_celery_tasks(values):
    time_0 = perf_counter()

    task_mul = mul.delay(values[0], values[1])
    output = task_mul.get()

    end_time = "%.6f" % (perf_counter() - time_0)

    return {'result': output, 'time': end_time}


def task_for_one_cpu():
    time_0 = perf_counter()

    print('task sent')
    for i in range(50):
        my_sort(5)

    end_time = "%.6f" % (perf_counter() - time_0)

    json_data = json.dumps({'time': end_time}, ensure_ascii=False)

    return json_data


def task_for_four_cpus():
    time_0 = perf_counter()

    done_tasks = []
    for i in range(50):
        done_tasks.append(my_sort.delay(5))

    print('all tasks sent')

    while done_tasks:
        for dt in done_tasks:
            if dt.state != 'PENDING':
                done_tasks.remove(dt)

    print('all tasks done')

    end_time = "%.6f" % (perf_counter() - time_0)

    json_data = json.dumps({'time': end_time}, ensure_ascii=False)

    return json_data
