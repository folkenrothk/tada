"""Handle the arguments provided to Tada"""

import argparse

from . import constants


def parse(args):
    """Use argparse to parse provided command-line arguments"""
    # create the parser with the default help formatter
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog='''Sample usage: python3 tada_a_bigoh.py --directory
            /Users/myname/projectdirectory
            --module modulename.file --function function_name --types int"''',
    )

    # add all of the arguments to the command-line interface
    parser.add_argument(
        "--directory",
        required=True,
        type=str,
        help="Package directory with functions to analyze",
    )
    parser.add_argument(
        "--module",
        required=True,
        type=str,
        help="Module name with functions to analyze",
    )
    parser.add_argument(
        "--function",
        required=True,
        type=str,
        help="Name of the module's function to analyze",
    )
    parser.add_argument(
        "--types",
        required=False,
        type=str,
        nargs="+",
        default=[],
        help="Parameter types for function to analyze",
    )
    parser.add_argument(
        "--startsize",
        required=False,
        type=int,
        default=constants.SIZE_START,
        help="The starting size of doubling experiment",
    )
    parser.add_argument(
        "--steps",
        required=False,
        type=int,
        default=constants.STEPS,
        help="The maximum rounds of experiment",
    )
    parser.add_argument(
        "--runningtime",
        required=False,
        type=int,
        default=constants.RUNNINGTIME,
        help="The maximum running time",
    )
    parser.add_argument(
        "--strategy", required=False, type=str, help="The path to the jsonschema"
    )
    # parse the arguments and return the finished result
    arguments_finished = parser.parse_args(args)
    return arguments_finished


def verify(args):
    """Verify the command-line arguments"""
    verified_arguments = False
    # CHECK: directory was specified and it is not ""
    if args.directory is not constants.NONE:
        verified_arguments = True
    # CHECK: module was specified and it is not ""
    if args.module is not constants.NONE:
        verified_arguments = True
    # CHECK: function was specified and it is not ""
    if args.function is not constants.NONE:
        verified_arguments = True
    return verified_arguments
