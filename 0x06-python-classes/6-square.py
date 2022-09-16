#!/usr/bin/python3

"""Define a class Square."""

class Square:
    
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
        self.__size = size

    def size(self):
        return (self.__size)

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)
    
    def my_print(self):
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]i
            [print("#", end="") for k in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
    
    def position(self):
        return (self.__position)
    def position(self, value):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
