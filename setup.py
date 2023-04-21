# -*- coding: utf-8 -*-
"""
Setup information for the project.
"""
from setuptools import find_packages, setup

setup(
    name="house_model",
    version="0.1.0",
    description="Electricity grid model of a house at KIT Energy Lab 2.0",
    author="Anja Hagen, Jan Ludwig, Simon Grafenhorst",
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=["pandapower",],
)

