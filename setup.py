from setuptools import setup, find_packages
import os

setup(
    # Application name:
    name="ru-neatest",

    # Version number:
    version="0.1",

    # Application author details:
    author="Sabin IO",
    author_email="hello@sabin.io",

    # Packages
    packages=find_packages(),

    # Data files
    include_package_data=True,
    zip_safe=False,

    # Details
    url="https://github.com/RichieBzzzt/ru-neatest",

    license="LICENSE",
    description="nunit test report generator to run in DataBricks",
    keywords='azure, databricks, nunit',
)
