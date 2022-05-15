import logging

from celery import shared_task

from app.core.constants.core_constants import CoreConstant
from app.core.draw_flag_scripts.flag import Flag3

logger = logging.getLogger(__name__)


@shared_task
def shared_task_draw_flag(even_number: int,
                          flag_obj_id: int) -> str:
    try:
        return Flag3(even_number, flag_obj_id).print_flag()
    except Exception as ex:
        logger.exception(f"shared_task_draw_flag(): Ex;"
                         f" {even_number = }, {flag_obj_id = };"
                         f" {ex = }")
        return CoreConstant.MDASH_SYMBOL
