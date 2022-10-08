#!/usr/bin/python3
"""Define a class Square"""

class Square(Rectangle):
    """Square constructor"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
