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
    bits = 0
    valid = True
    for i in data:
        lsb = 1 << 7
        if bits == 0:
            while i & lsb:  # 110xxxxx	10xxxxxx
                bits += 1
                lsb >>= 1
            if bits == 0:
                continue
        else:
            if bits < 5 and (i & lsb) and not (i & (1 << 6)):
                bits -= 1
            else:
                valid =  False

    return valid
