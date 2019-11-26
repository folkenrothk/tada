# Tada!: auTomAtic orDer-of-growth Analysis

[![Build Status](https://api.travis-ci.org/Tada-Project/tada.svg?branch=master)](https://travis-ci.org/Tada-Project/tada) [![codecov.io](http://codecov.io/github/Tada-Project/tada/coverage.svg?branch=master)](http://codecov.io/github/Tada-Project/tada?branch=master) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-orange.svg)](https://www.python.org/)

This repository contains the source code and usage instructions for a tool
called "Tada: auTomAtic orDer-of-growth Analysis" that is implemented in the
Python 3 language. The tool systematically runs a doubling experiment to
ascertain the likely worst-case order-of-growth function for an arbitrary Python
function. This documentation provides a brief overview about how to run the
tool, its provided test suite, and more. Please note that this is a work in
progress tool and potential future works are detailed in the `Future Works`
section below.

## Installing and Testing Tada

This program uses [Pipenv](https://github.com/pypa/pipenv) for installation.
Once you have installed `pipenv` you can run the test suite for Tada's functions
by typing the following in your terminal window:

- `pipenv install --dev`
- `pipenv shell`
- `pipenv run pytest`

If you want to collect the coverage of the provided test suite, then you can
run:

- `pipenv run pytest --cov-config pytest.cov --cov`

If you want to collect the coverage of the provided test suite and see what
lines of code are not covered, then you can run:

- `pytest --cov-config pytest.cov --cov --cov-report term-missing`

## Using Tada

Since the Tada tool is currently under heavy development, it is not yet feature
complete. In the future, its documentation will feature examples of how to run
the tool to automatically suggest the likely worst-case order-of-growth function
for a provided Python function.

If you want to run the tool, then you can run:

- `tada_a_bigoh.py [-h] --directory DIRECTORY --module MODULE --function FUNCTION --startsize STARTSIZE [--schema SCHEMA]`

You can learn about Tada's checks and defaults by typing python3
`tada_a_bigoh.py -h` in your terminal window and then reviewing the following
output.

```
usage: tada_a_bigoh.py [-h] --directory DIRECTORY --module MODULE --function
                       FUNCTION [--types TYPES [TYPES ...]]
                       [--startsize STARTSIZE] [--steps STEPS]
                       [--runningtime RUNNINGTIME] [--schema SCHEMA]

optional arguments:
  -h, --help            show this help message and exit
  --directory DIRECTORY
                        Package directory with functions to analyze (default:
                        None)
  --module MODULE       Module name with functions to analyze (default: None)
  --function FUNCTION   Name of the module's function to analyze (default:
                        None)
  --types TYPES [TYPES ...]
                        Parameter types for function to analyze (default: [])
  --startsize STARTSIZE
                        The starting size of doubling experiment (default: 1)
  --steps STEPS         The maximum rounds of experiment (default: 5)
  --runningtime RUNNINGTIME
                        The maximum running time (default: 200)
  --schema SCHEMA       The path to the jsonschema (default: None)
```

Tada adopts `Hypothesis` and `Hypothesis-jsonschema` to generate random data for the
provided Python function. Therefore, we encourage you to create a file of
a JSON array that contains JSON schemas for each parameter passed into the provided
function. Also, `Hypothesis` will raise warnings when generating data for functions
with `return` statements. In this version of Tada, we also encourage you remove the
`return` statements temporarily for the purpose of the experiment.

A sample of JSON schema for array can be found here: (speed-surprises)[https://github.com/Tada-Project/speed-surprises/blob/master/schema.json]
For further usage of JSON schemas and how to write them for various data types:
please refer to [JSON schema](https://json-schema.org/understanding-json-schema/reference/type.html)

When completed, Tada will be used to estimate the worst-case time complexity for
Python functions.

Here is an example of Tada being used in conjunction with functions in the
[Speed-Surprises repository](https://github.com/gkapfham/speed-surprises).

```
$ pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.lists.sorting --function insertion_sort --startsize 50 --schema ../speed-surprises/schema.json

🎆  Tada!: auTomAtic orDer-of-growth Analysis! 🎆
    https://github.com/gkapfhatm/tada
❓  For Help Information Type: python3 tada_a_bigoh.py -h  ❓

Start running experiment for size 50 →

.....................
tada_speedsurpriseslistssorting_insertionsort_50: Mean +- std dev: 6.07 ms +- 0.14 ms

Mean 0.006067049913023463
Median 0.006053275281374226
current indicator: 0.1
expected end time: 0.006067049913023463

→ Done running experiment for size 50

end time rate: 1
last end time rate: 1
Start running experiment for size 100 →
```

## Adding New Features to Tada

You can follow these steps to add a new feature if you are already a
collaborator on the project. If you want to add a new feature, please ensure
that it is accompanied by high coverage test cases and that you do not break any
of the existing test cases or features. First, you should type the following
command, substituting the name of your feature for the word `featurename`.

- `git checkout -b new-featurename`
- `git checkout master`
- `git push -u origin new-featurename`

Finally, you should open a pull request on the GitHub repository for the new
branch that you have created. This pull request should describe the new feature
that you are adding and give examples of how to run it on the command line. Of
course, if you are not a collaborator on this project, then you will need to
fork the repository, add your new feature, document and test it as appropriate,
and then create a pull request.

## Future Works

- Improve functionality of current analysis functions.
- Refactor code, specifically `tada_a_bigoh.py` file.
  - Consider making the functionality of generating the Results Table a class.
  - Consider separating the analysis features into separate functions.
- Clean up and reformat the output from the program to make it more readable
  and user friendly.

## Problems or Praise

If you have any problems with installing or using the Tada or its provided test
suite, then please create an issue associated with this Git repository using the
"Issues" link at the top of this site. The contributors to Tada will do all that
they can to resolve your issue and ensure that all of its features and the test
suite work well in your development environment.
