"""
run:
    python manage.py runscript config.queues_scripts.kill_workers
"""
import logging
import os
from time import sleep

logger = logging.getLogger(__name__)


def run():
    KillCeleryWorkers.kill_main_queue()


class KillCeleryWorkers:

    @staticmethod
    def kill_main_queue() -> None:
        try:
            stream = os.popen('ls ./logs/main_worker.pid')
            if main_pid_file := [i for i in str(stream.read()).split('\n') if i]:
                with open(main_pid_file[0], 'r') as main_pid_file_r:
                    main_pid_id = str(main_pid_file_r.read()).replace('\n', '')
                    os.system(f"kill -HUP {main_pid_id}")
        except Exception as ex:
            logger.error(f"kill_main_queue(): kill -HUP Ex;"
                         f" {ex = }")
        else:
            logger.info(f"kill_main_queue(): main queue pid stopped")
            sleep(2)

            if main_pid_file:
                try:
                    os.system(f"rm {main_pid_file[0]}")
                except Exception as ex:
                    logger.error(f"omg_restart_main_queue(): rm main_pid_file Ex;"
                                 f" {ex = }")

        return None
