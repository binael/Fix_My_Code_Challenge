#!/usr/bin/python3

""" A script that computes the area and perimeter of a square
"""


class Square():
    """
    A class that computes the size and area of square using the
    dimensions of the square
    Arguments:
        width: the width of the square
        height: the height of the square
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Instance Attributes"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the class"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
