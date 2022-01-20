from setuptools import setup

setup(
    name="Module",
    description="Simple python class and functions.",
    version="1.0",
    author="aw",
    author_email="none",
    packages=['Module'],
    entry_points={'console_scripts': ['zadanie8-awowra = Module.func:time']}
)
