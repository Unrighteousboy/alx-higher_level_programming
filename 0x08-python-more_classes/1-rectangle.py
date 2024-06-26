#!/usr/bin/python3

class Rectangle:

    def __init__(self, width=0, height=0):

        if (isinstance(width, int)):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError('width must be an integer')

        if (isinstance(height, int)):
            if height < 0:
                raise ValueError('height must be >= 0')
            self.__height = height
        else:
            raise TypeError('height must be an integer')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (isinstance(value, int)):
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (isinstance(value, int)):
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
        else:
            raise TypeError('height must be an integer')
