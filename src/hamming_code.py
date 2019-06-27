#!/usr/bin/env python3

from enum import Enum
from typing import List, Tuple, Union


# IMPORTANT NOTE: DO NOT IMPORT THE ev3dev.ev3 MODULE IN THIS FILE

class HCResult(Enum):
    """
    Return codes for the Hamming Code interface
    """
    VALID = 'OK'
    CORRECTED = 'FIXED'
    UNCORRECTABLE = 'ERROR'


class HammingCode:
    """
    -- TEMPLATE --
    Provides decoding capabilities for the specified Hamming Code
    """

    def __init__(self):
        """
        Initializes the class HammingCode with all values necessary.
        """
        self.total_bits = 0  # n
        self.data_bits = 0  # k
        self.parity_bits = 0  # r

        # Predefined non-systematic generator matrix G'
        g_ns = []

        # Convert non-systematic G' into systematic matrices G, H
        self.g = self.__convert_g(g_ns)
        self.h = self.__derive_h(self.g)

    def __convert_g(self, g_ns: List):
        """
        This method executes all steps necessary to convert G' into G.
        :param g_ns: List
        :return: List
        """
        # REPLACE "pass" WITH YOUR IMPLEMENTATION
        pass

    def __derive_h(self, g: List):
        """
        This method executes all steps necessary to derive H from G.
        :param g: List
        :return: List
        """
        # REPLACE "pass" WITH YOUR IMPLEMENTATION
        pass

    def encode(self, source_word: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Encodes the given source_word.
        :param source_word: 6-tuple
        :return: 11-tuple
        """
        # REPLACE "pass" WITH YOUR IMPLEMENTATION
        pass

    def decode(self, encoded_word: Tuple[int, ...]) -> Tuple[Union[None, Tuple[int, ...]], HCResult]:
        """
        Checks the channel alphabet word for errors and attempts to decode it.
        :param encoded_word: 11-tuple
        :returns: (6-tuple, HCResult) or (None, HCResult)
        """
        # REPLACE "pass" WITH YOUR IMPLEMENTATION
        pass

    def get_signature(self) -> Tuple[int, int, int]:
        """
        Returns signature of the Hamming Code.
        :return: 3-tuple
        """
        return self.total_bits, self.data_bits, self.parity_bits
