#!/usr/bin/env python3

import colorsys


class Color:
    def __init__(self, rgb):
        self.__r, self.__g, self.__b = rgb

    @property
    def hexcode(self):
        return '#{:02x}{:02x}{:02x}'.format(self.__r, self.__g, self.__b)

    @property
    def whiteness(self):
        return self.__r + self.__g + self.__b
