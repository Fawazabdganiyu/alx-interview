#!/usr/bin/python3
"""
UFT-8 encoding validation module
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Validate the given data set

    Args:
        data (List[int]): The list of integers to validate as utf-8 encoding

    Returns:
        bool: True if data is a valid utf-8 encoding else False
    """
    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) == 0b10:
                num_bytes -= 1
            else:
                return False

    return num_bytes == 0
