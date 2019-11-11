"""Constants used by the tada package"""

import os

# Parameters
SIZE_START = 1
FACTOR = 2
STEPS = 5
SIZE_STOP = SIZE_START * FACTOR ** STEPS
RUNNINGTIME = 200
INDICATOR = 0.1
STEP_START = 0

# Names
TADA = "tada"

# Separators
NONE = ""
PERIOD = "."
SEPARATOR = os.sep
SPACE = " "
UNDERSCORE = "_"

# Error codes
INCORRECT_ARGUMENTS = 2

# Directories
RESULTS = "_results"

# Files
SIZE = ".size.txt"
DIRECTORY = ".directory.txt"
CONFIGURATION = ".tada.json"

# Constants
UTF8 = "utf-8"

# Extensions
JSON_EXT = ".json"
PYTHON_EXT = ".py"

# Commands
PYTHON_EXEC = "python"

# Perf
DESCRIPTION_METANAME = "description"
PERF_BENCHMARK = "perf_benchmark"
