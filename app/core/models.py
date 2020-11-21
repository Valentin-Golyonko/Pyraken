from django.db import models


class Flag(models.Model):
    inner_circle_symbol = models.CharField(max_length=1, default='o')
    outer_circle_symbol = models.CharField(max_length=1, default='*')
    borders_symbol = models.CharField(max_length=1, default='#')
    free_space_symbol = models.CharField(max_length=12, default='&nbsp;&nbsp;')
    is_default_object = models.BooleanField(default=False, unique=True)
