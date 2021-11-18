
from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Get data from games where the api is available'
LONG_DESCRIPTION = 'Planning to get more game data...'

# Setting up
setup(
    name="GameData",
    version=VERSION,
    author="Ruthle55 (Thaddeus Teo)",
    author_email="<ruthle55.enquiries@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests','typing',''],
    keywords=['python','Games','Data','Game data'],
    classifiers=[
        "Development Status :: 1 - Developing",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)