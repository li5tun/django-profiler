import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-profiler',
    version='0.1',
    packages=['django_profiler'],
    description='use line_profiler to profile your views',
    long_description=README,
    author='Matt',
    author_email='li5tun@gmail.com',
    url='https://github.com/li5tun/django-profiler/',
    install_requires=[
        'Django>=1.11',
        'line-profiler>2.1'
    ]
)