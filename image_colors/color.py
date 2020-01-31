#!/usr/bin/env python3

import colorsys


class Color:
    def __init__(self, rgb):
        self.__r, self.__g, self.__b = rgb
        self.__hls = colorsys.rgb_to_hls(self.__r / 255, self.__g / 255,
                                         self.__b / 255)

    @property
    def hexcode(self):
        return '#{:02x}{:02x}{:02x}'.format(self.__r, self.__g, self.__b)

    @property
    def whiteness(self):
        return self.__r + self.__g + self.__b

    @property
    def saturation(self):
        return self.__hls[2]

    @property
    def hue(self):
        return self.__hls[0]
