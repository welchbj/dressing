"""Address resolution for Windows-based systems."""

import ctypes
import sys

from ctypes.util import (
    find_library)

from dressing._compat import (
    c_str_buf)
from dressing.errors import (
    DressingFunctionNotFoundException,
    DressingLibraryNotFoundException)
from dressing.utils import (
    win_only)

if sys.platform == 'win32':
    from ctypes.wintypes import (
        HMODULE,
        LPCSTR)


@win_only
def win_resolve_address(lib_name, func_name, absolute=False):
    """Get the resolved addresss of the specified lib / func combination.

    Args:
        lib_name (str): The name of the library in which to search.
        func_name (str): The name of the function whose address we will
            resolve.
        absolute (bool): If `True`, load the absolute address of the specified
            function in memory; otherwise, load the relative address using the
            loaded module's base address as the point of reference.

    Raises:
        DressingFunctionNotFoundException: If the function cannot be found in
            the specified library.
        DressingLibraryNotFoundException: If the library cannot be found on the
            system.

    Returns:
        int: The resolved address of the function.

    """
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel32.GetProcAddress.restype = ctypes.c_void_p
    kernel32.GetProcAddress.argtypes = (HMODULE, LPCSTR)

    try:
        lib_dll = ctypes.WinDLL(lib_name)
    except OSError:
        raise DressingLibraryNotFoundException(
            'Unable to find specified library `' + lib_name + '`')

    func_name_buf = c_str_buf(func_name)
    func_addr = kernel32.GetProcAddress(
        lib_dll._handle, func_name_buf)
    if not func_addr:
        raise DressingFunctionNotFoundException(
            'Unable to find function `' + func_name + '` in library `' +
            lib_name + '`')

    if absolute:
        return func_addr

    # compute relative address
    base_addr = lib_dll._handle
    offset = func_addr - base_addr
    return offset


@win_only
def win_find_lib(lib_name):
    """Find the full path to the specified library on Windows.

    Args:
        lib_name (str): The name of the library to find. This may be a full
            path, full name of the DLL, or partial name of the DLL.

    Raises:
        DressingLibraryNotFoundException: If the library cannot be found.

    Returns:
        str: The full path to the library.

    """
    lib_path = find_library(lib_name)
    if lib_path is None:
        raise DressingLibraryNotFoundException(
            'Unable to find library `' + lib_name + '`')
    return lib_path
