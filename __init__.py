"""Top-level package for usefulness."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """"""
__email__ = "you@gmail.com"
__version__ = "0.0.1"

from .src.usefulness.nodes import NODE_CLASS_MAPPINGS
from .src.usefulness.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
