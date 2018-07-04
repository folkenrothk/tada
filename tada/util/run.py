"""Run programs for Tada"""

import subprocess


def run_command(command):
    """Run a command and return the output and error code"""
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    output, error = process.communicate()
    return output, error


def run_benchmark(chosen_function, current_chosen_size):
    """Run a benchmark on a chosen_function and a current_chosen_size"""
    chosen_function(current_chosen_size)