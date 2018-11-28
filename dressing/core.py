"""Core functionality provided by this library."""

import sys

from dressing.win import (
    win_find_lib,
    win_resolve_address)


def resolve_address(lib_name, func_name):
    """Resolve the address of the specified function / library combination.

    Args:
        lib_name (str): The name of the library from which to resolve the
            function's address.
        func_name (str): The name of the function of which to resolve the
            address.

    Raises:
        DressingFunctionNotFoundException: If the function cannot be found.
        DressingLibraryNotFoundException: If the library cannot be found.

    Returns:
        int: The resolved address of the function.

    """
    if sys.platform == 'win32':
        return win_resolve_address(lib_name, func_name)
    else:
        raise NotImplementedError('Non-Windows implementation coming soon')


def find_lib(lib_name):
    """Find the path to the specified library name.

    Args:
        lib_name (str): The name of the library for which to search.

    Raises:
        DressingLibraryNotFoundException: If the library cannot be found.

    Returns:
        str: The full path to the library.

    """
    if sys.platform == 'win32':
        return win_find_lib(lib_name)
    else:
        raise NotImplementedError('Non-Windows implementation coming soon')
