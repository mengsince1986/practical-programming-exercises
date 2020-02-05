"""
6. Modify the file reader in read_smallest_skip.py of Skipping the Header,
on page 188, so that it uses a continue inside the loop instead of an if.
Which form do you find easier to read?
"""

from typing import TextIO
from io import StringIO
import time_series

def smallest_value(reader: TextIO) -> int:
    """Read and process reader and return the smallest value after the
    time_series header.

    >>> infile = StringIO('Example\\n1\\n2\\n3\\n')
    >>> smallest_value(infile)
    1
    >>> infile = StringIO('Example\\n3\\n1\\n2\\n')
    >>> smallest_value(infile)
    1
    """

    line = time_series.skip_header(reader).strip()

    if line != '':
        smallest  = int(line)

        for line in reader:
            line = line.strip()

            if line == '-':
                continue

            value = int(line)
            smallest = min(smallest, value)

        return smallest

if __name__ == '__main__':
    with open('hopedale.txt', 'r') as input_file:
        print(smallest_value(input_file))
