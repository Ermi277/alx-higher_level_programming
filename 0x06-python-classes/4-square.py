#!/usr/bin/python3

"""Define a class Square."""

class Square:

    """Represent a square."""
    def __init__(self, size=0):
        self.__size = size

    def size(self):
        return (self.__size)

    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

