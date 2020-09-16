# runeatest

[![Build Status](https://dev.azure.com/sabinio/sabin.io%20public/_apis/build/status/RichieBzzzt.runeatest?branchName=master)](https://dev.azure.com/sabinio/sabin.io%20public/_build/latest?definitionId=250&branchName=master)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

nunit test report generator to run in DataBricks

Add test case results to an object and at the end of testing. 
Convert results to a string that looks like a Nunit results file and exit notebook with string.

Do not use: Currently in planning phase.

## to do:

 * Merge test case results and present a complete nunit result file.
 * auto increment setup.py
 * publish to testpypi.
 * Setup a test notebook project that makes use of runeatest.
 * How to setup a job to execute notebook with tests.
 * Branching and branch policies/PR not sorted on the build.
 * Sort out build number

## known unknowns
 * How does this work with other types of jobs that can be run?


