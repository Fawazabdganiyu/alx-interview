#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """
from collections import defaultdict
import re
import sys


count = 0
file_size = 0
status_code = defaultdict(int)
for line in sys.stdin:
    line = line.strip()
    pattern = r'''
    ^                                     # The beginning of line
    (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})  # <IP Address>
    \s-\s                                 # Space, hyphen and space
    \[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{6})\] # [<date and time>]
    \s"GET\s/projects/260\sHTTP/1\.1"\s     # The GET request line
    (\d{3})\s(\d{1,4})                    # The status code and file size
    $                                     # The end of the line
    '''
    compiled_pattern = re.compile(pattern, re.VERBOSE)
    if compiled_pattern.match(line):
        count += 1
        file_size += int(line.split(' ')[-1])
        code = line.split(' ')[-2]
        status_code[code] += 1
        sorted_status_code = sorted(status_code)

        if count == 10:
            count = 0
            print(f'File size: {file_size}')
            for key in sorted_status_code:
                print(f'{key}: {status_code[key]}')
        if not line:
            break
