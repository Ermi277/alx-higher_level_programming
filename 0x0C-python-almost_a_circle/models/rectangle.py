#!/usr/bin/python3
"""Define class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Represent a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate Square or Rectangle"""
        return self.width * self.height

    def display(self):
        """Draw rectangle"""

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returnt rectangle dimension"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update rectangle"""
        if args and len(args) != 0:
            v = 0
            for arg in args:
                if v == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif v == 1:
                    self.width = arg
                elif v == 2:
                    self.height = arg
                elif v == 3:
                    self.x = arg
                elif v == 4:
                    self.y = arg
                v += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k== "x":
                    self.x = v
                elif k == "y":
                    self.y = v

