"""
1. Write a program that makes a backup of a file. Your program should prompt
the user for the name of the file to copy and then write a new file with the
same contents but with .bak as the file extension.
"""

from typing import TextIO

def backup_file(input_file: TextIO, output_file: TextIO) -> None:
    """ Read all the contents from reader and write all the contents to a new
    file with same name of reader and .bak as the file extension
    """

    for line in input_file:
        output_file.write(line)

    print("file has been copied")

if __name__ == '__main__':
    input_file_name = input('Please input a file name for backup: ')
    output_file_name = input_file_name + '.bak'
    with open(input_file_name, 'r') as input_file, \
            open(output_file_name, 'w') as output_file:
        backup_file(input_file, output_file)
