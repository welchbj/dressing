"""Command-line interface for `dressing`."""

from __future__ import print_function

import sys

from argparse import (
    ArgumentParser,
    RawTextHelpFormatter)

from dressing.core import (
    find_lib,
    resolve_address)
from dressing.errors import (
    DressingBaseException,
    DressingFunctionNotFoundException,
    DressingLibraryNotFoundException)
from dressing.version import (
    __version__)


def get_parsed_args(args=None):
    """Get the parsed command-line arguments."""
    parser = ArgumentParser(
        prog='dressing',
        usage='dressing LIBRARY FUNCTION',
        description=(
            'address resolution for you and your friends'),
        formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        '--version',
        action='version',
        version=str(__version__),
        help='program version')

    parser.add_argument(
        'library',
        action='store',
        metavar='LIBRARY',
        help='the library in which to search for the specified function')

    parser.add_argument(
        'function',
        action='store',
        metavar='FUNCTION',
        help='the function whose address you want to resolve')

    if args is None:
        args = sys.argv[1:]

    return parser.parse_args(args)


def main(args=None):
    """The main entrypoint into this tool."""
    try:
        opts = get_parsed_args(args)

        lib_path = find_lib(opts.library)
        addr = resolve_address(lib_path, opts.function)
        print(hex(addr))

        return 0
    except (DressingFunctionNotFoundException,
            DressingLibraryNotFoundException) as e:
        print(e, file=sys.stderr)
        return 1
    except DressingBaseException as e:
        print('Unexpected exception occured:', e, file=sys.stderr)
        return 1
    except Exception as e:
        print('Unknown exception occurred; re-raising it!', file=sys.stderr)
        raise e
