#!/usr/bin/python3
""" This program opens, reads and writes a file appending """


def append_write(filename="", text=""):
    """ this function writes a string to a text file (UTF8) and
    returns the number of characters written """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
