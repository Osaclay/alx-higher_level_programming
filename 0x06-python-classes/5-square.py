#!/usr/bin/python3
"""Documentation of a square class"""


class Square():
    """Square class of quadrilateral with four equal sides"""

    def __init__(self, size=0):
        """Sets initial size of the square object on instantiation
           Returns an error if the value given is not an integer
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
        Returns:
            the current size of the object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Resets size with a new value passed in
        Args:
            value (int): the new size to reset the object to
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
        """Returns area of the current object
        Returns:
            the area of the current square object
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square object"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
