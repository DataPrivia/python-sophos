# -*- coding: utf-8 -*-
"""Package Setup File for python-sophos"""
import setuptools


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='python-sophos',  
    version='0.1',
    scripts=[] ,
    author="Eli Keimig",
    author_email="eli.keimig@dataprivia.com",
    description="A Complete SDK for Sophos API Integration",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/dataprivia/python-sophos",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6+",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
)
