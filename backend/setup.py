# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "sportsbet_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="SportsBet Backend 0.1.1",
    author_email="rvabrilot@gmail.com",
    url="",
    keywords=["Swagger", "SportsBet Backend 0.1.1"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['sportsbet_server=sportsbet_server.__main__:main']},
    long_description="""\
    Esta API es del backend de SportsBet
    """
)
