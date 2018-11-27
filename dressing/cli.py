"""Command-line interface for `dressing`."""

from __future__ import print_function

import sys

from argparse import (
    ArgumentParser,
    RawTextHelpFormatter)

from dressing.version import (
    __version__)


def get_parsed_args(args=None):
    """Get the parsed command-line arguments."""
    parser = ArgumentParser(
        prog='dressing',
        usage='dressing [OPTIONS] LIBRARY FUNCTION',
        description='address resolution for you and your friends',
        formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        '--version',
        action='version',
        version=str(__version__),
        help='program version')

    if args is None:
        args = sys.argv[1:]

    return parser.parse_args(args)


def main(args=None):
    """The main entrypoint into this tool."""
    try:
        get_parsed_args(args)
    except Exception as e:
        print('Unknown exception occured; re-raising it!', file=sys.stderr)
        raise e
