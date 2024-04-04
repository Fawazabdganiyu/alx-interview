#!/usr/bin/python3
"""
UFT-8 encoding validation module
"""
from typing import List


def validUTF8(data: List) -> bool:
    """ Validate the given data set

    Args:
        data (list): The list of integers to validate as utf-8 encoding

    Returns:
        bool: True if data is a valid utf-8 encoding else False
    """
    num_bytes = 0
    for byte in data:
        lsb = 1 << 7
        if num_bytes == 0:
            while byte & lsb:  # 110xxxxx	10xxxxxx
                num_bytes += 1
                lsb >>= 1
            if num_bytes > 1:
                num_bytes -= 1
            if num_bytes == 1:
                return False
        else:
            if num_bytes < 4 and (byte & lsb) and not (byte & (1 << 6)):
                num_bytes -= 1
            else:
                return False

    return num_bytes == 0
