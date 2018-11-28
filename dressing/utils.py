"""Utilities for the `dressing` program."""

import os
import sys

from functools import (
    wraps)

from dressing.errors import (
    DressingPlatformException)


def posix_only(f):
    """Decorator marking ftions as *nix-only."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        if os.name != 'posix':
            raise DressingPlatformException(
                'Function cannot be called on non-POSIX systems')
        return f(*args, **kwargs)
    return wrapper


def win_only(f):
    """Decorator for marking ftions as Windows-only."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        if sys.platform != 'win32':
            raise DressingPlatformException(
                    'Function cannot be called on non-Windows systems')
        return f(*args, **kwargs)
    return wrapper
