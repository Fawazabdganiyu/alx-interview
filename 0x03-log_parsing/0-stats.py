#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """
from collections import defaultdict
import re
import sys


def print_metrics(current_file_size: int, current_status_codes: dict) -> None:
    """ Print out the metrics """
    sorted_status_code = sorted(current_status_codes)
    print(f'File size: {current_file_size}')
    for key in sorted_status_code:
        print(f'{key}: {current_status_codes[key]}')
        sys.stdout.flush()


def is_integer(input_str: str) -> bool:
    """ Checks if the provided string is an integer """
    try:
        int(input_str)
        return True
    except ValueError:
        return False


count = 0
total_size = 0
possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_codes = defaultdict(int)

pattern = r'''
^                                     # The beginning of line
(.+)                                  # <IP Address>
[\s\-\s]                              # Space, hyphen and space
\[.+\]                                # [<date and time>]
\s"GET\s/projects/260\sHTTP/1\.1"\s   # The GET request line
(.{3})\s(.{1,4})                      # The status code and file size
$                                     # The end of the line
'''
compiled_pattern = re.compile(pattern, re.VERBOSE)
try:
    for line in sys.stdin:
        line = line.strip()
        file_size = line.split(' ')[-1]
        if is_integer(file_size):
            total_size += int(file_size)
        if compiled_pattern.match(line):
            code = line.split(' ')[-2]
            if code in possible_codes and is_integer(code):
                count += 1
                status_codes[code] += 1
            if count % 10 == 0:
                print_metrics(total_size, status_codes)
finally:
    print_metrics(total_size, status_codes)
