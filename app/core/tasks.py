from __future__ import absolute_import, unicode_literals

import logging

from celery import shared_task

from app.core.draw_flag_scripts.flag import Flag3

logger = logging.getLogger(__name__)


@shared_task
def shared_task_draw_flag(even_number: int, flag_obj_id: int) -> str:
    logger.debug(f"shared_task_draw_flag(): even_number: {even_number}")
    return Flag3(even_number, flag_obj_id).print_flag()
