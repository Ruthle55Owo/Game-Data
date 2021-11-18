from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

VERSION = '0.1.1'
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
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=['requests','typing'],
    keywords=['python','Games','Data','Game data'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)