#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size

    def size(self):
        return (self.size)
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.size = size
    def area(self):
        return (self.size * self.size)
    def my_print(self):
        for i in range(0, self.size):
            [print("#", end="") for j in range(self.size)]
            print("")
        if self.size == 0:
            print("")

