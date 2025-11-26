#!/usr/bin/python3
"""Task 11"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Task 11"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = self

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        print(f"[Square] {width}/{height}")
