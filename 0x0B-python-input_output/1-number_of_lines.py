#!/usr/bin/python3
""" Program that returns the number of lines """


def number_of_lines(filename=""):
    """ function that returns the number of lines of a text file """
    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
