"""
run:
    python manage.py runscript celery_scripts.kill_workers
"""
import logging

from app.core.constants.core_constants import CoreConstant
from celery_scripts.restart_workers import RestartWorkers

logger = logging.getLogger(__name__)


def run() -> None:
    RestartWorkers.kill_celery_worker(
        worker_name=CoreConstant.DEFAULT_WORKER_NAME,
    )
    return None
