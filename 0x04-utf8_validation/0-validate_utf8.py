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
    def count_ones(current_data: int) -> int:
        """ Count the initial ones in the current code point
        """
        if current_data:
            binary = bin(current_data)[2:]
            count = 0
            for bit in binary:
                if bit == '0':
                    break
                else:
                    count += 1
            return count

    def validate(data: List, start: int, end: int) -> bool:
        """ Validate the set of code points
        """
        valid = True
        for i in range(start, end):
            binary = bin(data[i])[2:]
            if not binary.startswith('10'):
                valid = False
                break

        return valid

    valid = True
    for i in range(len(data)):
        ones = count_ones(data[i])
        if not ones:
            continue
        if ones != 1:
            try:
                valid = validate(data, i + 1, ones)
            except IndexError:
                valid = False
                break
        i = ones + 1

    return valid
