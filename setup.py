# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='salesforce microservice',
    version='0.0.1',
    description='Middleware application between Salesforce and custom applications ',
    long_description=readme,
    author='Walter Schweitzer',
    author_email='wschweitzer00@gmail.com',
    url='https://github.com/waltertschwe/python-salesforce-oauth',
    license=license,
    packages=find_packages(exclude=('docs'))
)
