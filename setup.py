#! /usr/bin/env python3
from setuptools import setup # type: ignore

import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name                =   "ScanSafe",
    version             =   '1.2',
    description         =   "The Multi-Tool Web Vulnerability Scanner.",
    long_description    =   README,
    long_description_content_type = "text/markdown",
    url                 =   "https://github.com/prakhar1684/ScanSafe",
    author              =   "prakhar",
    py_modules          =   ['scansafe',],
    install_requires    =   [],
    python_requires=">=3.6",
)
