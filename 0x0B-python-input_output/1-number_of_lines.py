#!/usr/bin/python3
""" This program returns the number of lines """


def number_of_lines(filename=""):
    """ This function returns the number of lines of a text file """
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return (count)
