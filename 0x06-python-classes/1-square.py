#!/usr/bin/python3
"""Documentation of a square class"""


class Square():
    """Square class of quadrilateral with four equal sides."""

    def __init__(self, size):
        """Sets initial size of the new square object
        Args:
            size (int): size of the square once instance is created
        """
        self.__size = size
