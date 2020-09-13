from setuptools import setup, find_packages
import os

setup(
    # Application name:
    name="runeatest",

    # Version number:
    version="0.18",

    # Application author details:
    author="Sabin IO",
    author_email="hello@sabin.io",

    # Packages
    packages=find_packages(),

    # Data files
    include_package_data=True,
    zip_safe=False,

    # Details
    url="https://github.com/RichieBzzzt/runeatest",

    description="nunit test report generator to run in DataBricks",
    long_description="Add test case results to an object and at the end of testing convert results to a string that looks like a Nunit results file and exit notebook with string.",
    keywords='azure, databricks, nunit',

     classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
