#!/usr/bin/python3
"""Initializes attributes of the class Square"""


class Square():
    """Models a square"""
    def __init__(self, size):
        """Initializes attributes of a square

        Args:
        size(int): The dimension of the new square"""

        self.__size = size
