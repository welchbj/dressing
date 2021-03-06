"""Address resolution for POSIX-based systems."""

import ctypes

from ctypes.util import (
    find_library)

from dressing._compat import (
    c_str_buf)
from dressing.errors import (
    DressingFunctionNotFoundException,
    DressingLibraryNotFoundException)
from dressing.utils import (
    posix_only)


class _Dl_info(ctypes.Structure):
    _fields_ = [
        ('dli_fname', ctypes.c_char_p),
        ('dli_fbase', ctypes.c_void_p),
        ('dli_sname', ctypes.c_char_p),
        ('dli_saddr', ctypes.c_void_p),
    ]


@posix_only
def posix_resolve_address(lib_name, func_name, absolute=False):
    """Get the resolved address of the specified lib / func combination.

    Args:
        lib_name (str): The name of the library in which to search.
        func_name (str): The name of the function for which to search.
        absolute (bool): If `True`, load the absolute address of the specified
            function in memory; otherwise, load the relative address using the
            loaded module's base address as the point of reference.

    Raises:
        DressingFunctionNotFoundException: If the function cannot be
            found in the specified library.
        DressingLibraryNotFoundException: If the library cannot be found
             on the system.

    Returns:
        int: The resolved address of the function.

    """
    libdl = ctypes.CDLL(find_library('dl'))
    libdl.dlsym.restype = ctypes.c_void_p
    libdl.dlsym.argtypes = (ctypes.c_void_p, ctypes.c_char_p)

    try:
        lib_dll = ctypes.CDLL(lib_name)
    except OSError:
        raise DressingLibraryNotFoundException(
            'Unable to find library + `' + lib_name + '`')

    func_name_buf = c_str_buf(func_name)
    func_addr = libdl.dlsym(lib_dll._handle, func_name_buf)
    if not func_addr:
        raise DressingFunctionNotFoundException(
            'Unable to find function `' + func_name + '` in library `' +
            lib_name + '`')

    if absolute:
        return func_addr

    # compute function offset
    libdl.dladdr.restype = ctypes.c_int
    libdl.dladdr.argtypes = (ctypes.c_void_p, ctypes.POINTER(_Dl_info))

    ret_dl_info = _Dl_info()
    res = libdl.dladdr(func_addr, ctypes.pointer(ret_dl_info))
    if not res:
        raise DressingLibraryNotFoundException(
            'Unable to look up shared library associated with address `' +
            hex(func_addr) + '`')

    base_addr = ret_dl_info.dli_fbase
    offset = func_addr - base_addr
    return offset


@posix_only
def posix_find_lib(lib_name):
    """Find the full name of the specified library on POSIX systems.

    Args:
        lib_name (str): The name of the library to find. This may be
            the full name of the library (i.e., `libc.so.6`) or the
            shortened name of the library (i.e., `c`).

    Raises:
        DressingLibraryNotFoundException: If the library cannot be found.

    Returns:
        str: The full name of the library.

    """
    full_lib_name = find_library(lib_name)
    if full_lib_name is not None:
        return full_lib_name

    try:
        ctypes.CDLL(lib_name)
    except OSError:
        raise DressingLibraryNotFoundException(
            'Unable to find library `' + lib_name + '`')

    return lib_name
