import logging
import math

from app.core.models import Flag

logger = logging.getLogger(__name__)


class Flag3:
    def __init__(self, number: int, flag_obj_id: int):
        flag_obj = self.get_flag_object(flag_obj_id)

        self.inner_circle_symbol = flag_obj.inner_circle_symbol
        self.outer_circle_symbol = flag_obj.outer_circle_symbol
        self.borders_symbol = flag_obj.borders_symbol
        self.free_space_symbol = flag_obj.free_space_symbol

        self._number = number

        self.inner_circle_radius = (self._number - 2) // 2
        self.outer_circle_radius = self.inner_circle_radius + 1
        self.circle_center_x = 1 + self._number + self.outer_circle_radius - 0.5
        self.circle_center_y = 1 + (self._number // 2) + self.outer_circle_radius - 0.5
        self.flag_width = 3 * self._number + 2
        self.flag_height = 2 * self._number + 2
        self.outer_radius_correction_coefficient = 0.18

    def circle_formula(self, x: int, y: int) -> str:
        """ x**2 + y**2 = r**2 """
        radius = math.sqrt((x - self.circle_center_x) ** 2 + (y - self.circle_center_y) ** 2)

        if radius <= self.inner_circle_radius:
            return self.inner_circle_symbol

        elif self.inner_circle_radius < radius <= self.outer_circle_radius:

            if abs(self.outer_circle_radius - radius) <= self.outer_radius_correction_coefficient:
                return self.free_space_symbol
            else:
                return self.outer_circle_symbol

        else:
            return self.free_space_symbol

    def create_flag(self) -> str:
        output_str = ''

        for y in range(self.flag_height):
            for x in range(self.flag_width):

                if (x == 0) or (x == self.flag_width - 1) or (y == 0) or (y == self.flag_height - 1):
                    output_str += self.borders_symbol
                else:
                    output_str += self.circle_formula(x, y)

            output_str += '<br>'

        return output_str

    def print_flag(self) -> str:
        return self.create_flag()

    @staticmethod
    def get_flag_object(flag_obj_id: int = None) -> Flag:
        try:
            if flag_obj_id:
                return Flag.objects.get(id=flag_obj_id)
            return Flag.objects.get(is_default_object=True)
        except Flag.DoesNotExist:
            logger.error(f"get_flag_object(): Flag.DoesNotExist")
            return Flag.objects.none()
        except Flag.DoesNotExist:
            logger.error(f"get_flag_object(): Flag.DoesNotExist")
            return Flag.objects.none()
