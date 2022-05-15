"""
RUN:
    python manage.py runscript config.queues_scripts.restart_queues

Some commands:
    celery -A config inspect active_queues

"""
import logging
import os
from time import sleep

from django.utils.timezone import now

from app.core.constants.core_constants import CoreConstant

logger = logging.getLogger(__name__)


def run():
    restart_main_queue()


def restart_main_queue() -> None:
    try:
        stream = os.popen('ls ./logs/main_worker.pid')
        if main_pid_file := [i for i in str(stream.read()).split('\n') if i]:
            with open(main_pid_file[0], 'r') as main_pid_file_r:
                main_pid_id = str(main_pid_file_r.read()).replace('\n', '')
                os.system(f"kill -HUP {main_pid_id}")
    except Exception as ex:
        logger.error(f"restart_main_queue(): kill -HUP Ex;"
                     f" {ex = }")
    else:
        logger.info(f"restart_main_queue(): main queue pid stopped")
        sleep(2)

        if main_pid_file:
            try:
                os.system(f"rm {main_pid_file[0]}")
            except Exception as ex:
                logger.error(f"restart_main_queue(): rm main_pid_file Ex;"
                             f" {ex = }")

    date_str = now().strftime(CoreConstant.Y_M_D_FORMAT)
    try:
        os.system(f"celery multi start worker"
                  f" -A config"
                  f" -l warning"
                  f" -c4"
                  f" -B"
                  f" -Q {CoreConstant.DEFAULT_QUEUE}"
                  f" -n pyraken_celery@%n"
                  f" --pidfile=./logs/main_%n.pid"
                  f" --logfile=./logs/main_%n_{date_str}.log")
    except Exception as ex:
        logger.error(f"restart_main_queue(): celery multi start worker Ex;"
                     f" {ex = }")
    else:
        logger.info(f"restart_main_queue(): main queue pid started")

    return None
