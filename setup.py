from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

VERSION = '0.1.2'
DESCRIPTION = 'Get data from api easier'
LONG_DESCRIPTION = 'Planning to get more game data...'

# Setting up
setup(
    name="EzApiData",
    version=VERSION,
    author="Ruthle55 (Thaddeus Teo)",
    author_email="<ruthle55.enquiries@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=['requests>=2.25.0','typing>=3.7.4'],
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