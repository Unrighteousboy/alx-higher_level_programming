#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise TypeError('size must be an integer')
        else:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (isinstance(value, int)):
            self.__size = value
            if value < 0:
                raise TypeError('size must be an integer')
        else:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size ** 2
