#!/usr/bin/python3

"""Define a class Square."""


class Square:
    
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        self._position = position
        self._size = size

    def size(self):
        return (self._size)

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self._size = value

    def area(self):
        return (self._size * self._size)
    
    def my_print(self):
        for i in range(0, self._size):
            [print(" ", end="") for j in range(0, self._position[0])]
            [print("#", end="") for k in range(self._size)]
            print(" ")
        if self.size == 0:
            print("")
    
    def position(self):
        return (self._position)

    def position(self, value):
        if not isinstance(position, tuple) or len(value) !=2 or \
                not all(isinstance(num, int) for num in value) \
                or not all(num >=0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value
