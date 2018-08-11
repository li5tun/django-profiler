import hashlib
import io
import inspect
import line_profiler

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from .models import Profile


def md5sum(file_path):
    md5 = hashlib.md5()
    with io.open(file_path, mode="rb") as fd:
        content = fd.read()
        md5.update(content)
    return md5.hexdigest()


class ProfilerMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        if getattr(settings, 'PAUSE_PROFILING', False):
            return None

        codes = inspect.getmodule(view_func).__dict__.values()
        request.profiler = line_profiler.LineProfiler()
        for code in codes:
            try:
                request.profiler.add_module(inspect.getmodule(code))
                request.mem_profiler.add_function(code)
            except AttributeError:
                continue
        request.profiler.enable_by_count()

    def process_response(self, request, response):
        if getattr(settings, 'PAUSE_PROFILING', False):
            return response

        ignore_dirs = getattr(settings, 'PROFILER_IGNORE_DIRS', [])

        if hasattr(request, 'profiler'):
            stats = request.profiler.get_stats().timings
            for entry in stats:
                if any(d in entry[0] for d in ignore_dirs):
                    continue

                if settings.BASE_DIR in entry[0]:
                    file_hash = md5sum(entry[0])
                    for column in stats[entry]:
                        Profile.objects.create(line=column[0],
                                               hits=column[1],
                                               time_consumed=column[2],
                                               func_name=entry[2],
                                               file_path=entry[0],
                                               file_hash=file_hash)
        return response
