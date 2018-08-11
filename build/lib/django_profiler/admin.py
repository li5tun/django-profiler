# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
     list_display = ('file_path', 'file_hash', 'func_name', 'line', 'hits', 'time_consumed', 'hit_at')


admin.site.register(Profile, ProfileAdmin)
