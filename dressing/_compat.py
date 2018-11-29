"""Handling Python 2/3 compatibility."""

import ctypes
import sys

IS_PY3 = sys.version_info >= (3, 0)


def c_str_buf(contents):
    """Create a C string buffer for use with ctypes.

    Args:
        contents (str): The raw string literal to pack into the buffer.

    Returns:
        The created ctypes string buffer.

    """
    if IS_PY3:
        contents = bytes(contents, encoding='utf-8')
    buf = ctypes.create_string_buffer(len(contents) + 1)
    buf.value = contents
    return buf
