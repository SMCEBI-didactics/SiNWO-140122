from setuptools import setup

setup(
    name="Module",
    description="Python function",
    version="1.0",
    author="lkiedos",
    author_email="none",
    packages=['Module'],
    entry_point={'console_scripts': ['zadanie8-lkiedos = modul.func:time']}
)
