"""Custom exception types for the `dressing` program."""


class DressingBaseException(Exception):
    """Base exception for the `dressing` program."""


class DressingLibraryNotFoundException(DressingBaseException):
    """Exception type for when libraries cannot be found."""


class DressingFunctionNotFoundException(DressingBaseException):
    """Exception type for when functions cannot be found within libraries."""
