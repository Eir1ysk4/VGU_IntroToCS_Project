# commands.py
from enum import Enum, auto


class Command(Enum):
    WEATHER = auto()
    PLAY = auto()
    WEB = auto()
    DATA = auto()
    # Add other commands as needed
