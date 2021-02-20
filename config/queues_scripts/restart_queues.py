"""
RUN:
python manage.py runscript config.queues_scripts.restart_queues

Some commands:
celery -A config inspect active_queues

"""
import logging
import os
from time import sleep

from config.settings import DEBUG

logger = logging.getLogger(__name__)


def run():
    if DEBUG:
        omg_restart_main_queue(log_lvl='info')
    else:
        omg_restart_main_queue()


def omg_restart_main_queue(log_lvl: str = 'warning') -> None:
    try:
        # os.system('pwd')
        # os.system('ls ./logs/worker.pid')
        stream = os.popen('ls ./logs/worker.pid')
        if main_pid_file := [i for i in str(stream.read()).split('\n') if i]:
            with open(main_pid_file[0], 'r') as main_pid_file_r:
                main_pid_id = str(main_pid_file_r.read()).replace('\n', '')
                os.system(f"kill -HUP {main_pid_id}")
    except Exception as ex:
        logger.error(f"omg_restart_main_queue(): {ex}")
    else:
        logger.info(f"omg_restart_main_queue(): main queue pid stopped")
        sleep(2)

    try:
        os.system(f"celery multi start worker -A config"
                  f" -c4 -B -l info --pidfile=./logs/%n.pid --logfile=./logs/%n.log")
    except Exception as ex:
        logger.error(f"omg_restart_main_queue(): {ex}")
    else:
        logger.info(f"omg_restart_main_queue(): main queue pid stared")

    return None
