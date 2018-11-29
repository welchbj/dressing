"""Setup configuration for the `dressing` program."""

import codecs
import os

from setuptools import (
    find_packages,
    setup)

HERE = os.path.abspath(os.path.dirname(__file__))
DRESSING_DIR = os.path.join(HERE, 'dressing')
VERSION_FILE = os.path.join(DRESSING_DIR, 'version.py')

with codecs.open(VERSION_FILE, encoding='utf-8') as f:
    exec(f.read())
    version = __version__  # noqa

setup(
    name='dressing',
    version=version,
    description='Address resolution for you and your friends',
    long_description='Visit the project\'s home page for more information',
    author='Brian Welch',
    url='https://github.com/welchbj/dressing',
    license='MIT',
    install_requires=[],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dressing = dressing.__main__:main'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities'
    ]
)
