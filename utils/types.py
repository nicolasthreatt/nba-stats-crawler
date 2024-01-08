"""
TYPES
"""
from enum import IntEnum, Enum, unique

@unique
class TableType(Enum):
    PLAYER = 1
    TEAM   = 2

@unique
class StorageType(IntEnum):
    INSERT = 1
    UPDATE = 2