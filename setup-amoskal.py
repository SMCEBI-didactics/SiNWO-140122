from setuptools import setup

setup(
    name='setup-file',
    version='1.0.0',
    description='short description of setup file',
    author='Adrian Moskal',
    author_email='adrian.moskal@smcebi.edu.pl',
    packages=['Module'],
    entry_points={
        'console_scripts': ['zadanie8-amoskal = modul.func:time']
        }
)
