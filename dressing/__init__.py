from .core import (  # noqa
    find_lib,
    resolve_address)
from .errors import (  # noqa
    DressingBaseException,
    DressingFunctionNotFoundException,
    DressingLibraryNotFoundException,
    DressingPlatformException)
from .posix import (  # noqa
    posix_find_lib,
    posix_resolve_address)
from .utils import (  # noqa
    posix_only,
    win_only)
from .win import (  # noqa
    win_find_lib,
    win_resolve_address)

# expose library version info
from .version import __version__ as _version, __version_info__ as _version_info
__version__ = _version
VERSION = _version
__version_info__ = _version_info
