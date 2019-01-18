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
    DressingLibraryNotFoundException,
    DressingPlatformException)
from dressing.version import (
    __version__)


def get_parsed_args(args=None):
    """Get the parsed command-line arguments."""
    parser = ArgumentParser(
        prog='dressing',
        usage='dressing LIBRARY FUNCTION',
        description=(
            '         8I\n'
            '         8I\n'
            '         8I                                           gg\n'
            '         8I                                           ""\n'
            '   ,gggg,8I   ,gggggg,   ,ggg,     ,g,       ,g,      gg    ,ggg,,ggg,     ,gggg,gg\n'       # noqa
            '  dP"  "Y8I   dP""""8I  i8" "8i   ,8\'8,     ,8\'8,     88   ,8" "8P" "8,   dP"  "Y8I\n'     # noqa
            ' i8\'    ,8I  ,8\'    8I  I8, ,8I  ,8\'  Yb   ,8\'  Yb    88   I8   8I   8I  i8\'    ,8I\n'  # noqa
            ' d8,   ,d8b,,dP     Y8, `YbadP\' ,8\'_   8) ,8\'_   8) _,88,_,dP   8I   Yb,,d8,   ,d8I\n'    # noqa
            ' "Y8888P"`Y88P      `Y8888P"Y888P\' "YY8P8PP\' "YY8P8P8P""Y88P\'   8I   `Y8P"Y8888P"888\n'   # noqa
            '                                                                               ,d8I\'\n'     # noqa
            '                                                                             ,dP\'8I\n'      # noqa
            '                                                                            ,8"  8I\n'       # noqa
            '                                                                            I8   8I\n'       # noqa
            '                                                                            `8, ,8I\n'       # noqa
            '                                                                             `Y8P"\n'        # noqa
            '                    address resolution for you and your friends'),
        formatter_class=RawTextHelpFormatter)

    parser.add_argument(
        '-o', '--offset',
        action='store_true',
        default=False,
        help='print the offset of the function within its loaded module')

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        default=False,
        help='increase detail of output')

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
        if opts.verbose:
            print('Using library at', lib_path)

        absolute = not opts.offset
        addr = resolve_address(lib_path, opts.function, absolute=absolute)
        print(hex(addr).rstrip('L'))

        return 0
    except (DressingFunctionNotFoundException,
            DressingLibraryNotFoundException) as e:
        print(e, file=sys.stderr)
        return 1
    except DressingPlatformException as e:
        print('Unexpected platform error occured:', e, file=sys.stderr)
        return 1
    except DressingBaseException as e:
        print('Unexpected exception occured:', e, file=sys.stderr)
        return 1
    except Exception as e:
        print('Unknown exception occurred; re-raising it!', file=sys.stderr)
        raise e
