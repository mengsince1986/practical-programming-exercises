"""
4. In Processing Whitespace-Delimited Data, on page 192, we used the “For Line
in File” technique to process data line by line, breaking it into pieces using
string method split. Rewrite function process_file to skip the header as normal
but then use the Read technique to read all the data at once.
"""

from typing import TextIO
from io import StringIO
import time_series

def find_largest(line: str) -> int:
    """Return the largest value in line, which is a whitespace-delimited string
    of integers that each end with a '.'.

    >>> find_largest('1. 3. 2. 5. 2.')
    5
    """

    # The largest value seen so far.
    largest = -1
    for value in line.split():
        # Remove the trailing period.
        v = int(value[:-1])
        # If we find a larger value, remember it.
        if v > largest:
            largest = v

    return largest

def process_file(reader: TextIO) -> int:
    """Read and process reader, which must start with a time_series header.
    Return the largest value after the header. There may be multiple pieces
    of data on each line.

    >>> infile = StringIO('Example\\n 20. 3.\\n 100. 17. 15.\\n')
    >>> process_file(infile)
    100
    """

    # read the first line
    line = time_series.skip_header(reader).strip()
    print(line)

    # read the rest of the file
    rest = reader.read().strip()
    print(rest)

if __name__ == '__main__':
    with open('lynx.txt', 'r') as input_file:
        process_file(input_file)
