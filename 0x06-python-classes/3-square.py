#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        sizes = self.__size ** 2
        return sizes
