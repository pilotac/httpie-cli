"""Machine-readable access to the HTTPie version."""
from typing import Tuple

from . import __version__


def version_tuple(version: str = __version__) -> Tuple[int, ...]:
    """Return the numeric release components, e.g. '3.2.4' -> (3, 2, 4)."""
    parts = []
    for part in version.split('.'):
        digits = ''.join(ch for ch in part if ch.isdigit())
        if not digits:
            break
        parts.append(int(digits))
    return tuple(parts)
