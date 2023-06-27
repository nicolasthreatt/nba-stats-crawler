"""
TYPES
"""
from enum import Enum, unique

@unique
class TableType(Enum):
    PLAYER = 1
    TEAM   = 2
