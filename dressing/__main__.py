"""Main entry point for the dressing program."""

import sys

from dressing.cli import main as cli_main

def main():
    """The function pointed to in console_scripts."""
    sys.exit(cli_main())


if __name__ == '__main__':
    main()
