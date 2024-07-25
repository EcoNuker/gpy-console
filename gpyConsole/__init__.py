"""
gpy-Console
"""

try:
    import guilded
except ImportError:
    RuntimeError("Cannot find guilded namespace please use:\n" "pip install guilded.py")

from gpyConsole.console import Console, Cog
from gpyConsole.converter import Converter
