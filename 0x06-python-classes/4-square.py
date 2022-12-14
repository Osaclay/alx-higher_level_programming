#!/usr/bin/python3
"""Documentation of a square class"""


class Square():
    """Square class of quadrilateral with four equal sides"""

    def __init__(self, size=0):
        """Sets size of the square on instantiation
           Retuns an error if the size passed in is not an integer
        Args:
            size (int, optional): the size of the square object
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

    @property
    def size(self):
        """Returns the current size of the object
           If called with a value, the setter function overwrites the
           current size with the size passed in
        Returns:
            size of the current object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Resets the size of the object with the value called
        Args:
            value (int): the new size of the square object
        Raises:
            TypeError: When the value passed in is not an integer
            ValueError: When the value passed in is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the current square object
        Returns:
            the area of the current square object
        """
        return self.__size ** 2
