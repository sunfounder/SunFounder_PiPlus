"""This is a module for PiPlus from SunFounder.

See:
https://www.sunfounder.com
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
import ds1307setup as DS1307
import sys

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SunFounder_PiPlus',
    version='1.2.0',
    description='SunFounder_PiPlus python module for Raspberry Pi',
    long_description=long_description,

    url='https://www.sunfounder.com',

    author='Cavon Lee',
    author_email='lijiarong@sunfounder.com',

    license='GNU',

    classifiers=[
        'Development Status :: 1 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        'Programming Language :: Python :: 2.7',
    ],

    keywords='Raspberry Pi',

    packages=find_packages(exclude=['example', 'docs', 'tests*']),

    install_requires=['RPi.GPIO'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={
        'PiPlus': ['package_data.dat'],
    },
    data_files=[('data', ['data/data_file'])],

    entry_points={
        'console_scripts': [
            'PiPlus=PiPlus:main',
        ],
    },
)

if len(sys.argv) > 2:
	if sys.argv[2] == '-c':
		DS1307.setup()
	elif sys.argv[2] == '--help':
		print 'use "-c" to setup DS1307 on Shield.' 
