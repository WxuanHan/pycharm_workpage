#!/usr/bin/env python3

from enum import IntEnum
from typing import Callable, Tuple
from ctypes import c_ubyte


# IMPORTANT NOTE: DO NOT IMPORT THE ev3dev.ev3 MODULE IN THIS FILE

class SMState(IntEnum):
    """
    Return codes for the stack machine
    """
    RUNNING = 1
    STOPPED = 2
    ERROR = 3


class StackMachine:
    """
    -- TEMPLATE --
    Implements the stack machine according to the specification
    """

    def __init__(self) -> None:
        """ Initialises the stack machine and its overflow flag """
        self.overflow = False

    def do(self, code_word: Tuple[int, int, int, int, int]) -> SMState:
        """
        Processes the entered code word by either executing the instruction or pushing the operand on the stack.
        :param code_word: 5-tuple
        :returns: SMState
        """
        # implementation
        pass

    def top(self) -> Tuple[int, int, int, int, int, int, int, int]:
        """
        Returns the top element of the stack.
        :returns: 8-tuple or None
        """
        # implementation
        pass
