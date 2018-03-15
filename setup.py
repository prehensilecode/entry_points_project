#!/usr/bin/env python3
import sys
from setuptools import setup

setup(name='my_project',
    version='0.0.4',
    packages=['my_project'],
    entry_points={
        'console_scripts': [
            'my_project = my_project.__main__:main',
            'do_something = my_project.__main__:do_something',
            'do_other = my_project.do_other:do_other',
            ### cannot do this -- "scripts" is interpreted as a module name
            #'elsewhere = scripts.elsewhere:elsewhere',
        ]
    },
)


