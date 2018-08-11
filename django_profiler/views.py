# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import View

from .models import Task


def add(a, b):
    return a + b


def home(request):
    s = 0
    for item in [(1, 2), (3, 4), (5, 6)]:
        s += add(item[0], item[1])
    return HttpResponse(s)


class HomeView(View):
    def add(self, a, b):
        return a + b

    def get(self, request):
        s = 0
        for item in [(1, 2), (3, 4), (5, 6)]:
            s += self.add(item[0], item[1])
        task, created = Task.objects.get_or_create(name='test', defaults={'content': 'testing'})
        return HttpResponse(task.get_uppercase_name())
