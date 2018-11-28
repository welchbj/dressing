"""Utilities for the `dressing` program."""

import os
import sys

from functools import (
    wraps)

from dressing.errors import (
    DressingPlatformException)


def posix_only(func):
    """Decorator marking functions as *nix-only."""
    @wraps(func)
    def check_posix(func):
        if os.name != 'posix':
            raise DressingPlatformException(
                'Function cannot be called on non-POSIX systems')


def win_only(func):
    """Decorator for marking functions as Windows-only."""
    @wraps(func)
    def check_win(func):
        if sys.platform != 'win32':
            raise DressingPlatformException(
                    'Function cannot be called on non-Windows systems')
    return check_win
