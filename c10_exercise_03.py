"""
3. All of the file-reading functions we have seen in this chapter read forward
through the file from the first character or line to the last. How could you
write a function that would read backward through a file?
"""

from typing import TextIO
from io import StringIO

def read_reverse(reader: TextIO) -> str:
    """read contents from reader into a single string in a reverse direction.

    >>> input_file = StringIO('line1\nline2\nline3\n')
    >>> read_reverse(input_file)
    'line3\nline2\nline1\n'
    """
    reverse_str = ""

    for item in reversed(file_2_list(reader)):
        reverse_str += item

    return reverse_str

def readlines_reverse(reader: TextIO) -> list:
    """read contents from reader into a list with the contents in a reverse
    direction.

    >>> input_file = StringIO('line1\nline2\nline3\n')
    >>> readlines_reverse(input_file)
    ['line3\n', 'line2\n', 'line1\n']
    """

    reverse_lst = []

    for item in reversed(file_2_list(reader)):
        reverse_lst.append(item)

    return reverse_lst

def reverse_file(reader: TextIO) -> TextIO:
    """reverse the contens of the reader and return the reversed contents into
    a TextIO
    """
    return StringIO(read_reverse(reader))

# utilities
def file_2_list(reader: TextIO) -> str:
    """read contens from reader into a list.

    >>> input_file = StringIO('line1\nline2\nline3\n')
    >>> file_2_list(input_file)
    ['line1\n', 'line2\n', 'line3\n']
    """
    return reader.readlines()

if __name__ == '__main__':
    with open('file_example.txt', 'r') as input_file:
        print(read_reverse(input_file))
        print('-------')

    with open('file_example.txt', 'r') as input_file:
        print(readlines_reverse(input_file))
        print('-------')

    with open('file_example.txt', 'r') as input_file:
        reversed_file = reverse_file(input_file)
        print(reversed_file.readline())
        print(reversed_file.readline())
        print(reversed_file.readline())
        print('-------')
