from enum import Enum


class Status(Enum):

    PASS = 1
    FAIL = 2
    INFO = 3
    FATAL = 4
    ERROR = 5
    WARNING = 6
    SKIP = 7
    UNKNOWN = 8

