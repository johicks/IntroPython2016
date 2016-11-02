#!/usr/bin/env python


def read_file(file):
    with open(file, 'r') as f:
        read_data = f.read()
    f.closed
    return read_data


if __name__ == '__main__':
    print(read_file('sherlock_small.txt'))
