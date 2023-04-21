# -*- coding: utf-8 -*-
"""
Setup information for the project.

Code initally generated for the Praktikum: Smart Energy System Lab.
"""
from setuptools import find_packages, setup

setup(
    name="22_p4_building_model",
    version="0.1.0",
    description="Project to model the electricity house of Energy Lab 2.0",
    author="Anja Hagen & Jan Ludwig",
    packages=find_packages(exclude=("tests", "docs")),
)

