================
Django Profiler
================

Django profiler based line_profiler to save profile info into DB

Quick start
____________


1. Add `django_profiler` to your INSTALLED_APPS

2. Add `django_profiler.middleware.ProfilerMiddleware` to MIDDLEWARE

3. `PAUSE_PROFILING = True` disable the profiling, default is False

4. PROFILER_IGNORE_DIRS = [], ignore some dirs, e.g. ['django_profiler', 'venv']
