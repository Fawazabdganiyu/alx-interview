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


def main():
    count = 0
    file_size = 0
    possible_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    status_codes = defaultdict(int)

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
    try:
        for line in sys.stdin:
            line = line.strip()
            if compiled_pattern.match(line):
                count += 1
                file_size += int(line.split(' ')[-1])
                code = int(line.split(' ')[-2])
                if code in possible_codes:
                    status_codes[code] += 1

                if not count % 10:
                    print_metrics(file_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)


if __name__ == '__main__':
    main()
