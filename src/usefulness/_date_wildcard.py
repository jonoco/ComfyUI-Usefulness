import re
from datetime import datetime, timezone


# Ordered longest-first to avoid partial token replacement (e.g. 'MM' before 'M')
_FORMAT_MAP = [
    ("yyyy", "%Y"),
    ("MM",   "%m"),
    ("dd",   "%d"),
    ("hh",   "%H"),
    ("mm",   "%M"),
    ("ss",   "%S"),
]

_WILDCARD_RE = re.compile(r"%date:([^%]+)%", re.IGNORECASE)


def _convert_format(fmt: str) -> str:
    for token, directive in _FORMAT_MAP:
        fmt = fmt.replace(token, directive)
    return fmt


def expand_date_wildcards(path: str) -> str:
    """Replace all ``%date:FORMAT%`` wildcards in *path* with the current UTC time.

    Example::

        expand_date_wildcards("/output/%date:yyyy-MM-dd-hhmmss%/file.txt")
        # -> "/output/2026-03-28-191501/file.txt"
    """
    now = datetime.now(timezone.utc)

    def _replace(match: re.Match) -> str:
        fmt = _convert_format(match.group(1))
        return now.strftime(fmt)

    return _WILDCARD_RE.sub(_replace, path)
