# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Profile(models.Model):
    line = models.SmallIntegerField(verbose_name='Line Number')
    hits = models.SmallIntegerField(verbose_name='Hits')
    time_consumed = models.DecimalField(verbose_name='Time Consumed', max_digits=16, decimal_places=4)
    func_name = models.CharField(verbose_name='Function Name', max_length=256)
    file_path = models.CharField(verbose_name='File Path', max_length=256)
    file_hash = models.CharField(verbose_name='File Hash', max_length=32)
    hit_at = models.DateTimeField(verbose_name='Hit at', auto_now_add=True)

    def __str__(self):
        return self.file_path


@python_2_unicode_compatible
class Task(models.Model):
    name = models.CharField(verbose_name='Name', max_length=32)
    content = models.TextField(verbose_name='Content', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_uppercase_name(self):
        upper_name = self.name.upper()
        return upper_name
