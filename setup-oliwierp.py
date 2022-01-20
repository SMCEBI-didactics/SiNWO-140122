from setuptools import setup

setup(
	name="Module",
	description="Zadanie 8",
	version="1.0",
	author="oliwierp",
	author_emial="oliwier.pszeniczko@smcebi.edu.pl",
	packages=['Module'],
    entry_points={'console_scripts': ['zadanie8-oliwierp = Module.func:time']}
)
