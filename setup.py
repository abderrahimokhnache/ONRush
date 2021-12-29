from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "readme.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Basic NO-SQL Packages Built upon SQLite'
LONG_DESCRIPTION = 'rush-db makes working with data base easy by taking all the heavy stuff'

# Setting up
setup(
    name="Rush_db",
    version=VERSION,
    author="astroxiii (abderrahim mokhnache)",
    author_email="<abderrahimokhnache@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'sqlite', 'sql', 'no-sql', 'db', 'database'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)