#!/usr/bin/env python3

from enum import IntEnum
from typing import List, Tuple, Union
from ctypes import c_ubyte


# IMPORTANT NOTE: DO NOT IMPORT THE ev3dev.ev3 MODULE IN THIS FILE

class SMState(IntEnum):
    """
    Return codes for the stack machine
    """
    RUNNING = 1
    STOPPED = 0
    ERROR = -1


class StackMachine:
    """
    -- TEMPLATE --
    Implements the 8-bit stack machine according to the specification
    """

    def __init__(self) -> None:
        """
        Initializes the class StackMachine with all values necessary.
        """
        self.overflow = False
        self.stack = []

    def do(self, code_word: Tuple[int, ...]) -> SMState:
        """
        Processes the entered code word by either executing the instruction or pushing the operand on the stack.
        :param code_word: 6-tuple
        :returns: SMState
        """
        # REPLACE "pass" WITH YOUR IMPLEMENTATION
        pass

    def top(self) -> Union[None, str, Tuple[int, int, int, int, int, int, int, int]]:
        """
        Returns the top element of the stack.
        :returns: 8-tuple or None
        """
        # REPLACE "pass" WITH YOUR IMPLEMENTATION
        pass
