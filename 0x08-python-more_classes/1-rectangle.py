#!/usr/bin/python3

"""Define a class Rectangle"""

class Rectangle:
    
    """Represent a class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = widt
        self.height = height

    def width(self):
        return self.width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.width = value

    def height(self):
        return self.height
    
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            slef.height = height
