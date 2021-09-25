#!/usr/bin/env python3

from setuptools import setup, find_packages

# Minimal setup configuration.
setup(
    name="rahul_exp_lib",
    packages=find_packages(exclude=("*tests",)),
)