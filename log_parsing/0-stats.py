#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import re
import sys

PATTERN = re.compile(
    r'^\S+ - \[.+\] "GET /projects/260 HTTP/1.1" (\S+) (\d+)$')
CODES = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_stats(total, counts):
    """Prints the file size and the number of lines per status code"""
    print("File size: {}".format(total))
    for code in CODES:
        if counts[code] > 0:
            print("{}: {}".format(code, counts[code]))


def main():
    """Parses stdin and prints stats every 10 lines and on CTRL + C"""
    total = 0
    lines = 0
    counts = dict((code, 0) for code in CODES)
    try:
        for line in sys.stdin:
            match = PATTERN.match(line.strip())
            if match is None:
                continue
            code, size = match.groups()
            total += int(size)
            if code in counts:
                counts[code] += 1
            lines += 1
            if lines % 10 == 0:
                print_stats(total, counts)
        print_stats(total, counts)
    except KeyboardInterrupt:
        print_stats(total, counts)
        raise


if __name__ == "__main__":
    main()
