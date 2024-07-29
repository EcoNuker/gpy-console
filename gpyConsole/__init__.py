"""
gpy-Console
"""

__version__ = "0.1.1a"

try:
    import guilded
except ImportError:
    RuntimeError("Cannot find guilded namespace please use:\n" "pip install guilded.py")

from gpyConsole.console import ConsoleClient, ConsoleBot
from gpyConsole.converters import Converter
