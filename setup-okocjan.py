from setuptools import setup

setup(
    name="dev-okocjan",
    description="Zadanie 8 i 9",
    version="1.0",
    author="okocjan",
    author_email="oskar.kocjan@smcebi.edu.pl",
    license="MIT",
    packages=['Module'],
    entry_points={'console_scripts': ['zadanie8-okocjan = Module.func:time']}
)
