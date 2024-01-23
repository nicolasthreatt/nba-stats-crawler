from enum import IntEnum, unique

@unique
class TableType(IntEnum):
    PLAYER = 1
    TEAM   = 2
