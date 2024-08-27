#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':

    total_file_size = 0
    line_count = 0
    valid_status_codes =
    ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_code_counts = {code: 0 for code in valid_status_codes}

    def print_statistics(status_code_counts: dict, total_file_size: int)
    -> None:
        print("File size: {:d}".format(total_file_size))
        for status_code, count in sorted(status_code_counts.items()):
            if count:
                print("{}: {}".format(status_code, count))

    try:
        for line in sys.stdin:
            line_count += 1
            line_parts = line.split()
            try:
                status_code = line_parts[-2]
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except IndexError:
                pass
            try:
                file_size = int(line_parts[-1])
                total_file_size += file_size
            except (IndexError, ValueError):
                pass
            if line_count % 10 == 0:
                print_statistics(status_code_counts, total_file_size)
        print_statistics(status_code_counts, total_file_size)
    except KeyboardInterrupt:
        print_statistics(status_code_counts, total_file_size)
        sys.exit(0)
