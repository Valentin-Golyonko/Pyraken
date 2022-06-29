"""
run:
    python manage.py runscript celery_scripts.restart_workers

"""
import logging
import os
from time import sleep

from django.utils.timezone import now

from app.core.constants.core_constants import CoreConstant
from config.settings import DEBUG

logger = logging.getLogger(__name__)


def run() -> None:
    RestartWorkers.restart_workers()
    return None


class RestartWorkers:

    @classmethod
    def restart_workers(cls) -> None:
        if DEBUG:
            log_lvl = 'info'
        else:
            log_lvl = 'warning'

        date_str = now().strftime(CoreConstant.Y_M_D_FORMAT)

        cls.restart_main_queue(
            log_lvl=log_lvl,
            log_date=date_str,
        )
        # +other queue
        return None

    @classmethod
    def restart_main_queue(cls, log_lvl: str, log_date: str) -> None:
        """
        1. find main worker pid file
        2. kill main worker
        3. start new main worker (concurrency not specified -> worker uses all available cores / v-threads)
        """
        cls.kill_celery_worker(
            worker_name=CoreConstant.DEFAULT_WORKER_NAME,
        )
        cls.start_celery_worker(
            worker_name=CoreConstant.DEFAULT_WORKER_NAME,
            queue_name=CoreConstant.DEFAULT_QUEUE,
            concurrency_number=CoreConstant.DEFAULT_CONCURRENCY,
            log_lvl=log_lvl,
            log_date=log_date,
        )
        return None

    @staticmethod
    def kill_celery_worker(worker_name: str) -> None:
        try:
            stream = os.popen(f"ls ./logs/{worker_name}_worker.pid")
            if worker_pid_file := [i for i in str(stream.read()).split('\n') if i]:
                with open(worker_pid_file[0], 'r') as pid_file:
                    pid_id = str(pid_file.read()).replace('\n', '')
                    os.system(f"kill -HUP {pid_id}")
                    pid_file.close()
        except Exception as ex:
            msg = f"kill_celery_worker(): kill -HUP Ex; {worker_name = }; {ex = }"
            logger.error(msg)
            # SendToSentry.send_msg(msg, CoreConstant.SENTRY_MSG_EXCEPTION)
        else:
            logger.info(f"kill_celery_worker(): celery worker stopped; {worker_name = }")
            sleep(2)

            if worker_pid_file:
                try:
                    os.system(f"rm {worker_pid_file[0]}")
                except Exception as ex:
                    msg = f"kill_celery_worker(): rm worker_pid_file Ex; {worker_name = }; {ex = }"
                    logger.error(msg)
                    # SendToSentry.send_msg(msg, CoreConstant.SENTRY_MSG_EXCEPTION)

        return None

    @staticmethod
    def start_celery_worker(worker_name: str,
                            queue_name: str,
                            concurrency_number: int,
                            log_lvl: str,
                            log_date: str) -> None:
        try:
            os.system(f"celery multi start worker"
                      f" -A config"
                      f" -l {log_lvl}"
                      f" -c{concurrency_number}"
                      f" -B"
                      f" -Q {queue_name}"
                      f" -n pyraken_queue_{queue_name}@%n"
                      f" --pidfile=./logs/{worker_name}_%n.pid"
                      f" --logfile=./logs/{worker_name}_%n_{log_date}.log")
        except Exception as ex:
            msg = f"start_celery_worker(): celery multi start worker Ex;" \
                  f" {worker_name = }, {queue_name = }; {ex = }"
            logger.error(msg)
            # SendToSentry.send_msg(msg, CoreConstant.SENTRY_MSG_EXCEPTION)
        else:
            logger.info(f"start_celery_worker(): celery worker started")

        return None
