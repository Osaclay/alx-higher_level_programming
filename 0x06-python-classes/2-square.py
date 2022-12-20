#!/usr/bin/python3
"""Documentation of a square class"""


class Square():
    """Square class of a quadrilateral with four equal sides"""

    def __init__(self, size=0):
        """Sets size of the square on instantation
           Returns an error if size called with it is not an integer
        Args:
            size (int, optional): The size of the square object
        Raises:
            TypeError: When the value passed in is not an integer
            ValueError: When the value passed in is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
