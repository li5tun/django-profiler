# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mock import patch, Mock
from django.conf import settings
from django.test import TestCase

from .models import Profile
from .middleware import ProfilerMiddleware


class ProfilerMiddlewareTestCase(TestCase):
    @patch('django_profiler.middleware.ProfilerMiddleware')
    def test_init(self, middleware_mock):
        middleware = ProfilerMiddleware('response')
        self.assertEqual(middleware.get_response, 'response')

    @patch('django_profiler.middleware.md5sum')
    def test_middleware(self, md5sum_mock):
        md5sum_mock.return_value = '55555'
        request = Mock()
        request.profiler.get_stats.return_value.timings = {
            (settings.BASE_DIR+'/abc/', 0, 'add'): [(10, 1, 150), (11, 2, 60)],
            ('/blah/', 0, 'sub'): [(11, 1, 200)]
        }
        middleware = ProfilerMiddleware(Mock())
        middleware(request)
        self.assertEqual(Profile.objects.count(), 2)
